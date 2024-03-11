package engine.AIs;


import chess_rules.Board;
import chess_rules.Move;
import engine.OutOfTimeException;
import engine.Response;
import engine.evaluators.CPWEval;
import engine.evaluators.Evaluator;
import engine.evaluators.StandardEval;

public class AlphaBeta implements AI {

    private boolean timeToStop;
    private Evaluator evaluator = new CPWEval();

    // Data from last run

    public Response getBestResponse(Board board, int depth) throws OutOfTimeException {
        return getResponse(board.copy(), new Response(), depth, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private Response getResponse(Board board, Response currentResponse, double currentDepth, int alpha, int beta) throws OutOfTimeException{

        if (timeToStop) {
            throw new OutOfTimeException();
        }

        Move bestMove = null;
        Response bestResponse = null;
        int bestEvaluation = 0;

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        /* Base Case */

        int isBoardCheckOrStaleMate = board.isBoardCheckOrStaleMate();
        if (isBoardCheckOrStaleMate != 0) {
            if (isBoardCheckOrStaleMate == Board.DRAW) {
                currentResponse.setResultingEvaluation(0);
                return currentResponse;
            } else if (isBoardCheckOrStaleMate == Board.WHITE_WON) {
                currentResponse.setResultingEvaluation(1000);
                return currentResponse;
            } else if (isBoardCheckOrStaleMate == Board.BLACK_WON) {
                currentResponse.setResultingEvaluation(-1000);
                return currentResponse;
            }
        }
        if (currentDepth < 0.5) {
            currentResponse.setResultingEvaluation(evaluator.getEvaluation(board));
            return currentResponse;
        }

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        // Test principal variation

        if (board.getTurn() == Board.WHITE) {

            bestEvaluation = Integer.MIN_VALUE;

            for (Move move: board.getAllPossibleMoves()) {

                board.movePiece(move);
                Response response;
                if (move.isCapture() && currentDepth <= 1) {
                    response = getResponse(board, currentResponse, currentDepth - 0.25, alpha, beta);
                } else {
                    response = getResponse(board, currentResponse, currentDepth - 1, alpha, beta);
                }
                board.reverseMove(move);

                int evaluation = response.getResultingEvaluation();

                if (evaluation > bestEvaluation) {
                    bestEvaluation = response.getResultingEvaluation();
                    bestMove = move;
                    bestResponse = response;
                }

                // Alpha Beta Pruning:
                alpha = Integer.max(alpha, evaluation);

                if (beta <= alpha) {
                    break;
                }

            }


        } else if (board.getTurn() == Board.BLACK) {

            bestEvaluation = Integer.MAX_VALUE;

            for (Move move: board.getAllPossibleMoves()) {
                board.movePiece(move);
                Response response;

                if (move.isCapture() && currentDepth <= 1) {
                    response = getResponse(board, currentResponse, currentDepth - 0.25, alpha, beta);
                } else {
                    response = getResponse(board, currentResponse, currentDepth - 1, alpha, beta);
                }

                board.reverseMove(move);
                int evaluation = response.getResultingEvaluation();

                if (evaluation < bestEvaluation) {
                    bestEvaluation = response.getResultingEvaluation();
                    bestMove = move;
                    bestResponse = response;
                }

                // Alpha Beta Pruning:
                beta = Integer.min(beta, evaluation);

                if (beta <= alpha) {
                    break;
                }
            }
        }

        Response newResponse = new Response();
        newResponse.getMoveList().add(bestMove);
        assert bestResponse != null;
        newResponse.getMoveList().addAll(bestResponse.getMoveList());
        newResponse.setResultingEvaluation(bestEvaluation);

        return newResponse;
    }

    public void start() {
        timeToStop = false;
    }

    public void stop() {
        timeToStop = true;
    }

}
