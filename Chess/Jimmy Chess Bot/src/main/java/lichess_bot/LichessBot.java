package lichess_bot;

import au.com.anthonybruno.lichessclient.LichessClient;
import au.com.anthonybruno.lichessclient.handler.GameEventHandler;
import au.com.anthonybruno.lichessclient.handler.UserEventHandler;
import au.com.anthonybruno.lichessclient.model.event.GameStart;
import chess_rules.Board;
import chess_rules.Move;
import com.fasterxml.jackson.databind.node.ObjectNode;
import engine.AIs.AI;
import engine.AIThread;
import engine.AIs.AlphaBeta;
import engine.AIs.Aspiration;
import engine.Response;

class LichessBot {
    private String currentGameId = "";
    private String apiToken;
    private String me;
    private boolean challenger;
    private String opponent;
    private int timeLimit;


    LichessBot(String apiToken, String me, boolean challenger, String opponent, int timeLimit) {
        this.apiToken = apiToken;
        this.challenger = challenger;
        this.opponent = opponent;
        this.me = me;
        this.timeLimit = timeLimit;

        new UserEventThread().start();
    }

    class UserEventThread extends Thread {
        LichessClient userEventClient;

        @Override
        public void run() {
            userEventClient = new LichessClient(apiToken);

            try {
                if (challenger) {
                    userEventClient.createChallenge(opponent, true);
                }
            } catch (Exception ignored) {}

            userEventClient.streamIncomingEvents(new MyUserEventHandler());
        }

        void halt() {
            try {
                userEventClient.close();
            } catch (Exception ignored) {}
        }

        class MyUserEventHandler implements UserEventHandler {

            @Override
            public void incomingChallenge(ObjectNode challengeEvent) {
                currentGameId = challengeEvent.get("challenge").get("id").asText();
                userEventClient.acceptChallenge(currentGameId);
            }

            @Override
            public void gameStart(GameStart gameStartEvent) {
                currentGameId = gameStartEvent.getId();
                new GameEventThread().start();
                halt();
            }
        }
    }

    class GameEventThread extends Thread {
        LichessClient gameEventClient;

        Board gameBoard;
        AI ai;
        AIThread aiThread;

        @Override
        public void run() {
            gameBoard = new Board();
            gameBoard.newGame();
            ai = new Aspiration();
            aiThread = new AIThread(gameBoard, ai);
            gameEventClient = new LichessClient(apiToken);
            gameEventClient.streamGameState(currentGameId, new MyGameEventHandler());
        }

        public void halt() {
            try {
                gameEventClient.close();
            } catch (Exception ignored) {}
        }

        class MyGameEventHandler implements GameEventHandler {

            //
            int colorPlaying;


            @Override
            public void chatReceived(ObjectNode chat) {
                if (!chat.get("username").asText().equals(me)) {
                    gameEventClient.writeInChat(currentGameId, "player", "Your chat has been received!");
                }
            }

            @Override
            public void fullGameState(ObjectNode gameState) {

                System.out.println("FULL GAME STATE: " + gameState);

                currentGameId = gameState.get("id").asText();
                gameBoard.newGame();
                for (String move: gameState.get("state").get("moves").asText().split(" ")) {
                    if (move.length() > 0) {
                        updateBoard(move);
                    }
                }

                // Figures out what side is being played
                if (gameState.get("white").get("id") != null && gameState.get("white").get("id").asText().equals(me)) {
                    colorPlaying = Board.WHITE;
                } else {
                    colorPlaying = Board.BLACK;
                }

                if (colorPlaying == gameBoard.getTurn()) {
                    makeAIMove();
                }

            }

            @Override
            public void gameStateUpdate(ObjectNode gameState) {
                // Check for what kind of update

                String movesString = gameState.get("moves").asText();
                String[] movesArray = movesString.split(" ");
                String lastMoveString = movesArray[movesArray.length - 1].substring(0,4);

                System.out.println(lastMoveString);

                if (isMyTurn(gameState.get("moves").asText())) {
                    updateBoard(lastMoveString);
                    makeAIMove();
                }
            }

            void makeAIMove() {
                gameBoard.printBoard();

                aiThread = new AIThread(gameBoard, ai);
                aiThread.start();
                try {
                    Thread.sleep(timeLimit);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                Response response = aiThread.getBestResponse();
                aiThread.finish();
                try {
                    aiThread.join();
                } catch (Exception e) {
                    e.printStackTrace();
                }

                String botPlay = gameBoard.getUCI(response.getMoveList().get(0));
                gameBoard.movePiece(response.getMoveList().get(0));
                gameEventClient.makeMove(currentGameId, botPlay);
            }

            void updateBoard(String moveString) {
                Move move = gameBoard.createMove(moveString);
                gameBoard.movePiece(move);
                testEnd();
            }

            void testEnd() {
                if (gameBoard.isBoardCheckOrStaleMate() != 0) {
                    try {
                        gameEventClient.close();
                    } catch (Exception ignored) {}
                    new UserEventThread().start();
                }
            }

            boolean isMyTurn(String moves) {
                // if true then white's turn else black's turn
                boolean turn = moves.split(" ").length % 2 == 0;
                return turn && colorPlaying == Board.WHITE || !turn && colorPlaying == Board.BLACK;
            }
        }

    }

}
