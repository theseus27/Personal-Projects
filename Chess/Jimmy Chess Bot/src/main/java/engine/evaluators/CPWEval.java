package engine.evaluators;

import chess_rules.Board;
import chess_rules.Move;
import chess_rules.Square;

public class CPWEval implements Evaluator{

    /*
    Current State:
        - New material evaluation
        - Middle game mobility

    Next Steps:
        - Include endgame weight
     */

    @Override
    public int getEvaluation(Board board) {

        // TODO: Update material values
        // material
        int materialEvaluation = 0;
        for (Square[] row: board.squares) {
            for (Square square: row) {
                if (square.containsPiece()) {
                    if (square.pieceColor == Board.WHITE) {
                        materialEvaluation += Board.pieceValues.get(square.pieceID);
                    } else if (square.pieceColor == Board.BLACK) {
                        materialEvaluation -= Board.pieceValues.get(square.pieceID);
                    }
                }

            }
        }

        // mobility
        int middleGameMobilityScore = 0;
        int endGameMobilityScore = 0;

        // 0 = black
        // 1 = white

        int[] numKnightMoves = new int[2];
        int[] numBishopMoves = new int[2];
        int[] numKingMoves = new int[2];
        int[] numQueenMoves = new int[2];

        for (int i = 0; i < 2; i++) {
            // Do both current and opposite turn
            for (Move move: board.getAllPossibleMoves()) {
                if (move.getPieceValue() == 2) {
                    Square square = board.squares[move.getStartRow()][move.getStartCol()];
                    if (square.pieceColor == Board.BLACK) {
                        numKnightMoves[0] += 1;
                    } else {
                        numKnightMoves[1] += 1;
                    }
                } else if (move.getPieceValue() == 3) {
                    Square square = board.squares[move.getStartRow()][move.getStartCol()];
                    if (square.pieceColor == Board.BLACK) {
                        numBishopMoves[0] += 1;
                    } else {
                        numBishopMoves[1] += 1;
                    }
                } else if (move.getPieceValue() == 5) {
                    Square square = board.squares[move.getStartRow()][move.getStartCol()];
                    if (square.pieceColor == Board.BLACK) {
                        numQueenMoves[0] += 1;
                    } else {
                        numQueenMoves[1] += 1;
                    }
                } else if (move.getPieceValue() == 6) {
                    Square square = board.squares[move.getStartRow()][move.getStartCol()];
                    if (square.pieceColor == Board.BLACK) {
                        numKingMoves[0] += 1;
                    } else {
                        numKingMoves[1] += 1;
                    }
                }
            }
            board.toggleTurn();
        }


        // Knight
        middleGameMobilityScore += knightMobilityEvaluator(numKnightMoves[1]) - knightMobilityEvaluator(numKnightMoves[0]);
        endGameMobilityScore += knightMobilityEvaluator(numKnightMoves[1]) - knightMobilityEvaluator(numKnightMoves[0]);

        // Bishop
        middleGameMobilityScore += bishopMobilityEvaluator(numBishopMoves[1]) - bishopMobilityEvaluator(numBishopMoves[0]);
        endGameMobilityScore += bishopMobilityEvaluator(numBishopMoves[1]) - bishopMobilityEvaluator(numBishopMoves[0]);

        // Rook
        for (Square[] row: board.squares) {
            for (Square square: row) {
                if (square.pieceID == 4) {
                    // Check for half open
                    boolean isHalfOpen = true;
                    boolean isOpen = true;
                    for (int rowNum = 0; rowNum < 8; rowNum ++) {
                        Square currentSquare = board.squares[rowNum][square.getCol()];
                        if (currentSquare.pieceID == 1) {
                            isOpen = false;
                            if (currentSquare.pieceColor != square.pieceColor) {
                                isHalfOpen = false;
                            }
                        }
                    }

                    if (isOpen) {
                        middleGameMobilityScore += 10;
                        endGameMobilityScore += 10;
                    } else if (isHalfOpen) {
                        middleGameMobilityScore += 5;
                        endGameMobilityScore += 5;
                    }
                }
            }
        }

        // King
        middleGameMobilityScore += kingMobilityMiddlegameEvaluator(numKingMoves[1]) - kingMobilityMiddlegameEvaluator(numKingMoves[0]);
        endGameMobilityScore += kingMobilityEndgameEvaluator(numKingMoves[1]) - kingMobilityEndgameEvaluator(numKingMoves[0]);

        // Queen
        middleGameMobilityScore += queenMobilityMiddlegameEvaluator(numQueenMoves[1]) - queenMobilityMiddlegameEvaluator(numQueenMoves[0]);
        endGameMobilityScore += queenMobilityEndgameEvaluator(numQueenMoves[1]) - queenMobilityEndgameEvaluator(numQueenMoves[0]);

        int middleGameScore = middleGameMobilityScore + materialEvaluation;
        int endGameScore = endGameMobilityScore + materialEvaluation;

        return middleGameScore;
    }

    private int knightMobilityEvaluator(int numKnightMoves) {
        return 4 * (numKnightMoves - 4);
    }

    private int bishopMobilityEvaluator(int numBishopMoves) {
        return 3 * (numBishopMoves - 7);
    }

    private int queenMobilityMiddlegameEvaluator(int numQueenMoves) {
        return numQueenMoves - 14;
    }

    private int queenMobilityEndgameEvaluator(int numQueenMoves) {
        return 2 * (numQueenMoves - 14);
    }

    private int kingMobilityMiddlegameEvaluator(int numKingMoves) {
        return 2 * (numKingMoves - 7);
    }

    private int kingMobilityEndgameEvaluator(int numKingMoves) {
        return 4 * (numKingMoves - 7);
    }

}
