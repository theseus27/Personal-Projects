package engine.evaluators;

import chess_rules.Board;
import chess_rules.Square;

public class StandardEval implements Evaluator{
    public int getEvaluation(Board board) {
        int evaluation = 0;

        int numWhiteMoves = 0;
        int numBlackMoves = 0;
        for (Square[] row: board.squares) {
            for (Square square: row) {
                if (square.containsPiece()) {
                    if (square.pieceColor == Board.WHITE) {
                        evaluation += Board.pieceValues.get(square.pieceID);
                        numWhiteMoves += board.getMoves(square).size();
                    } else if (square.pieceColor == Board.BLACK) {
                        evaluation -= Board.pieceValues.get(square.pieceID);
                        numBlackMoves += board.getMoves(square).size();
                    }
                }

            }
        }

        evaluation -= ((double) numBlackMoves) * 0.1;
        evaluation += ((double) numWhiteMoves) * 0.1;

        return evaluation;
    }
}
