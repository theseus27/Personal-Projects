package chess_rules;

public class Square {
    int row;
    int col;
    public int pieceID;
    public int pieceColor;

    public boolean isHighlighted;
    public boolean isPossibleMove;

    Square(int row, int col) {
        this.row = row;
        this.col = col;
    }

    private Square(int row, int col, int pieceID, int pieceColor) {
        this.row = row;
        this.col = col;
        this.pieceID = pieceID;
        this.pieceColor = pieceColor;
    }

    void addPiece(int pieceID, int pieceColor) {
        this.pieceID = pieceID;
        this.pieceColor = pieceColor;
    }

    public boolean containsPiece() {
        return pieceID > 0;
    }

    void movePiece(Square newSquare) {
        newSquare.pieceID = pieceID;
        newSquare.pieceColor = pieceColor;
        pieceID = 0;
        pieceColor = 0;
    }

    void removePiece() {
        this.pieceID = 0;
        this.pieceColor = 0;
    }

    Square copy() {
        return new Square(row, col, pieceID, pieceColor);
    }

    boolean equals(Square square) {
        return row == square.row && col == square.col && pieceID == square.pieceID && pieceColor == square.pieceColor;
    }

    public String toString() {
        return Move.colConversions.get(col) + "" + Move.rowConversions.get(row);
    }

    public int getRow() {
        return row;
    }

    public int getCol() {
        return col;
    }
}
