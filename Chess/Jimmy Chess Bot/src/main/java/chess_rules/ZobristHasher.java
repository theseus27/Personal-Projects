package chess_rules;

import java.util.Random;

public class ZobristHasher {

    // Table values

    private long[][][] zobristTable;
    private long[] colOfValidEnPassant;
    private long sideToMoveIsBlack;
    private long whiteCastleQueenside;
    private long blackCastleQueenside;
    private long whiteCastleKingside;
    private long blackCastleKingside;

    private final long initialBoardValue = 0;

    private Random random;

    ZobristHasher() {
        zobristTable = new long[8][8][12];
        colOfValidEnPassant = new long[8];
        random = new Random(65789);
        initializeTable();
    }

    void initializeTable() {
        for (int x = 0; x < zobristTable.length; x ++) {
            for (int y = 0; y < zobristTable[x].length; y ++) {
                for (int z = 0; z < zobristTable[x][y].length; z ++) {
                    zobristTable[x][y][z] = random.nextLong();
                }
            }
        }
        for (int x = 0; x < colOfValidEnPassant.length; x++) {
            colOfValidEnPassant[x] = random.nextLong();
        }
        sideToMoveIsBlack = random.nextLong();
        whiteCastleQueenside = random.nextLong();
        blackCastleQueenside = random.nextLong();
        whiteCastleKingside = random.nextLong();
        blackCastleKingside = random.nextLong();
    }

    long getHash(Board board) {
        long hash = initialBoardValue;

        for (int row = 0; row < 8; row ++) {
            for (int col = 0; col < 8; col ++) {
                Square square = board.getSquare(row, col);
                if (square.containsPiece()) {
                    hash ^= zobristTable[row][col][getPieceTableLocation(square.pieceID, square.pieceColor)];
                }
            }
        }

        if(board.getTurn() == Board.BLACK) {
            hash ^= sideToMoveIsBlack;
        }

        if (board.whiteCastleQueenside()) {
            hash ^= whiteCastleQueenside;
        }
        if (board.blackCastleQueenside()) {
            hash ^= blackCastleQueenside;
        }
        if (board.whiteCastleKingside()) {
            hash ^= whiteCastleKingside;
        }
        if (board.blackCastleKingside()) {
            hash ^= blackCastleKingside;
        }

        if (board.hasEnPassant()) {
            Square enPassantSquare = board.enPassantSquare();
            int tableCol = enPassantSquare.col;
            hash ^= colOfValidEnPassant[tableCol];
        }

        return hash;
    }

    int getPieceTableLocation(int pieceID, int pieceColor) {
        /*
        0 - white pawn
        ...
        6 - black pawn
         */

        int location = 0;

        if (pieceColor == Board.WHITE) {
            location = pieceID - 1;
        } else if (pieceColor == Board.BLACK) {
            location = pieceID + 5;
        }

        return location;
    }
}
