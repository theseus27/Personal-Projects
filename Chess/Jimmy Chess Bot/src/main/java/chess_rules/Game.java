package chess_rules;

import java.util.ArrayList;

public class Game {

    public boolean hasGameStarted;
    public boolean isGameOver;
    public Board currentBoard;

    private ArrayList<Board> previousBoards;

    private int fiftyMoveCount;

    public Game(){
        hasGameStarted = false;
        currentBoard = new Board();
        previousBoards = new ArrayList<>();
    }

    public void move(Move move) {

        previousBoards.add(currentBoard.copy());
        Square s1 = currentBoard.getSquare(move.startRow, move.startCol);
        Square s2 = currentBoard.getSquare(move.endRow, move.endCol);

        // Update 50 move count
        if (s1.pieceID == 1 || s2.pieceID != 0) {
            fiftyMoveCount = 0;
        } else {
            fiftyMoveCount ++;
        }

        currentBoard.movePiece(move);
    }

    public void startNewGame() {
        hasGameStarted = true;
        isGameOver = false;
        currentBoard.newGame();
        previousBoards.clear();
    }

    /**
     0 - Game is not over
     1 - Game is a draw
     2 - White has won
     3 - Black has won
     */
    public int isGameOver() {

        int isCheckOrStalemate = currentBoard.isBoardCheckOrStaleMate();
        if (isCheckOrStalemate > 0) {
            isGameOver = true;
            return isCheckOrStalemate;
        } else {
            isGameOver = true;
            // Check for 50 move repetition
            if (fiftyMoveCount >= 100) {
                return Board.DRAW;
            }

            // Check for three move repetition
            int numReps = 0;
            for (Board board: previousBoards) {
                if (board.equals(currentBoard)) {
                    numReps ++;
                }
            }
            if (numReps >= 3) {
                return Board.DRAW;
            }

            isGameOver = false;

            // Not checkmate or draw
            return Board.GAME_IN_PROGRESS;
        }
    }

    public boolean isAITurn(boolean compIsWhite, boolean compIsBlack) {
        return (currentBoard.getTurn() == Board.WHITE && compIsWhite) || (currentBoard.getTurn() == Board.BLACK && compIsBlack);
    }

}
