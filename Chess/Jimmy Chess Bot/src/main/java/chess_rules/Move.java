package chess_rules;

import java.util.HashMap;

public class Move {
    int pieceValue;

    int startCol;
    int startRow;

    int endCol;
    int endRow;

    boolean isPromotion;
    int endPieceValue;

    boolean isCapture;
    int capturedPieceValue;
    int capturedPieceColor;

    boolean isCastleQueenside;
    boolean isCastleKingside;
    boolean isEnPassant;

    boolean isFirstWhiteKingMove;
    boolean isFirstBlackKingMove;
    boolean isFirstWhiteKingRookMove;
    boolean isFirstWhiteQueenRookMove;
    boolean isFirstBlackKingRookMove;
    boolean isFirstBlackQueenRookMove;

    Square newEnPassantSquare;
    Square previousEnPassantSquare;

    static HashMap<Integer, String> pieceConversions;
    static HashMap<Integer, String> rowConversions;
    static HashMap<Integer, String> colConversions;

    static {
        pieceConversions = new HashMap<>();
        pieceConversions.put(1, "");
        pieceConversions.put(2, "N");
        pieceConversions.put(3, "B");
        pieceConversions.put(4, "R");
        pieceConversions.put(5, "Q");
        pieceConversions.put(6, "K");

        rowConversions = new HashMap<>();
        rowConversions.put(0, "8");
        rowConversions.put(1, "7");
        rowConversions.put(2, "6");
        rowConversions.put(3, "5");
        rowConversions.put(4, "4");
        rowConversions.put(5, "3");
        rowConversions.put(6, "2");
        rowConversions.put(7, "1");

        colConversions = new HashMap<>();
        colConversions.put(0, "a");
        colConversions.put(1, "b");
        colConversions.put(2, "c");
        colConversions.put(3, "d");
        colConversions.put(4, "e");
        colConversions.put(5, "f");
        colConversions.put(6, "g");
        colConversions.put(7, "h");
    }

    Move(int startRow, int startCol, int endRow, int endCol, int pieceValue) {
        this.startRow = startRow;
        this.startCol = startCol;
        this.endRow = endRow;
        this.endCol = endCol;
        this.pieceValue = pieceValue;
    }

    @Override
    public String toString() {
        String moveString = pieceConversions.get(pieceValue);
        if (isCapture) {
            moveString += "x";
        }
        moveString += colConversions.get(endCol) + "" + rowConversions.get(endRow);
        if (isEnPassant) {
            moveString += " [en passant]";
        }
        return moveString;
    }

    public boolean isCapture() {
        return isCapture;
    }

    public int getPieceValue() {
        return pieceValue;
    }

    public int getStartRow() {
        return startRow;
    }

    public int getStartCol() {
        return startCol;
    }

    public int getEndCol() {
        return endCol;
    }

    public int getEndRow() {
        return endRow;
    }
}
