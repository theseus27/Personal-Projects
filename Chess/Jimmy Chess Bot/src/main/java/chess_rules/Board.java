package chess_rules;

import java.util.ArrayList;
import java.util.HashMap;

/*
Current limitations:
- Promotion will only promote to Queen
- IsGameOver does not work for insufficient material
 */

public class Board {

    // Use this to detect three move repetition
    private static ZobristHasher zobristHasher = new ZobristHasher();

    ///////////////////////////////////////////////////

    public static final int GAME_IN_PROGRESS = 0;
    public static final int DRAW = 1;
    public static final int WHITE_WON = 2;
    public static final int BLACK_WON = 3;
    public static final int WHITE = -1;
    public static final int BLACK = 1;
    public static HashMap<Integer, Integer> pieceValues;
    private static HashMap<String, Integer> reverseRowNames;
    private static HashMap<String, Integer> reverseColNames;

    static {
        pieceValues = new HashMap<>();
        pieceValues.put(0, 0);
        pieceValues.put(1, 100);
        pieceValues.put(2, 325);
        pieceValues.put(3, 335);
        pieceValues.put(4, 500);
        pieceValues.put(5, 975);
        pieceValues.put(6, 0);

        reverseRowNames = new HashMap<>();
        reverseRowNames.put("1", 7);
        reverseRowNames.put("2", 6);
        reverseRowNames.put("3", 5);
        reverseRowNames.put("4", 4);
        reverseRowNames.put("5", 3);
        reverseRowNames.put("6", 2);
        reverseRowNames.put("7", 1);
        reverseRowNames.put("8", 0);

        reverseColNames = new HashMap<>();
        reverseColNames.put("a", 0);
        reverseColNames.put("b", 1);
        reverseColNames.put("c", 2);
        reverseColNames.put("d", 3);
        reverseColNames.put("e", 4);
        reverseColNames.put("f", 5);
        reverseColNames.put("g", 6);
        reverseColNames.put("h", 7);

    }

    //////////////////////////////////////////////////

    // Change to array of ints
    public Square[][] squares;

    //////////////////////////////////////////////////

    /* Move-specific values */

    private int turn;
    private int plyNumber;

    //////////////////////////////////////////////////

    /*
    The value of the int denotes which move the piece was moved
    If the value is negative, the piece has not been moved
     */

    private boolean hasWhiteKingMoved;
    private boolean hasBlackKingMoved;
    private boolean hasWhiteKingRookMoved;
    private boolean hasWhiteQueenRookMoved;
    private boolean hasBlackKingRookMoved;
    private boolean hasBlackQueenRookMoved;

    //////////////////////////////////////////////////

    /*
    Denotes whether or not an en passant move is possible on a given turn
    If en passant is not possible, value is null
     */

    private Square possibleEnPassant;

    //////////////////////////////////////////////////

    private long hash;

    //////////////////////////////////////////////////

    /* Get/Set functions */

    // returns the current turn.
    public int getTurn() {
        return turn;
    }

    // Gets a square on the board
    public Square getSquare(int row, int col) {
        return squares[row][col];
    }

    public ArrayList<Move> getAllPossibleMoves(){
        ArrayList<Move> allPossibleMoves = new ArrayList<>();
        for (Square[] row: squares) {
            for (Square square: row) {
                if (square.pieceColor == turn) {
                    for (Move move: getMoves(square)) {
                        if (tryMove(move)) {
                            allPossibleMoves.add(move);
                        }
                    }
                }
            }
        }
        return allPossibleMoves;
    }

    // TODO: add promotion
    public void movePiece(Move move) {

        // Update ply number
        plyNumber ++;

        // Find beginning and end squares of move
        Square s1 = squares[move.startRow][move.startCol];
        Square s2 = squares[move.endRow][move.endCol];

        // Changes the turn
        changeTurn();

        if (move.isFirstWhiteKingMove) {
            hasWhiteKingMoved = true;
        } else if (move.isFirstBlackKingMove) {
            hasBlackKingMoved = true;
        } else if (move.isFirstBlackQueenRookMove) {
            hasBlackQueenRookMoved = true;
        } else if (move.isFirstBlackKingRookMove) {
            hasBlackKingRookMoved = true;
        } else if (move.isFirstWhiteQueenRookMove) {
            hasWhiteQueenRookMoved = true;
        } else if (move.isFirstWhiteKingRookMove) {
            hasWhiteKingRookMoved = true;
        }

        // Do move and check for king move and castling
        if (s1.pieceID == 6) {
            // castling
            if (move.isCastleKingside) {
                if (s1.pieceColor == WHITE) {
                    squares[7][7].movePiece(squares[7][5]);
                } else {
                    squares[0][7].movePiece(squares[0][5]);
                }
            } else if (move.isCastleQueenside) {
                if (s1.pieceColor == WHITE) {
                    squares[7][0].movePiece(squares[7][3]);
                } else {
                    squares[0][0].movePiece(squares[0][3]);
                }
            }
        } else if (s1.pieceID == 1) {
            if (move.isPromotion) {
                s1.pieceID = move.endPieceValue;
            } else if (move.isEnPassant) {
                squares[move.startRow][move.endCol].pieceID = 0;
            }
        }

        possibleEnPassant = move.newEnPassantSquare;

        s1.movePiece(s2);

        // updateHash(move);
    }

    public void reverseMove(Move move) {
        // Update ply number
        plyNumber --;

        Square s1 = squares[move.startRow][move.startCol];
        Square s2 = squares[move.endRow][move.endCol];

        // Changes the turn
        changeTurn();

        // Check if removing a king move
        if (move.isFirstWhiteKingMove) {
            hasWhiteKingMoved = false;
        } else if (move.isFirstWhiteKingRookMove) {
            hasWhiteKingRookMoved = false;
        } else if (move.isFirstWhiteQueenRookMove) {
            hasWhiteQueenRookMoved = false;
        } else if (move.isFirstBlackKingMove) {
            hasBlackKingMoved = false;
        } else if (move.isFirstBlackKingRookMove) {
            hasBlackKingRookMoved = false;
        } else if (move.isFirstBlackQueenRookMove) {
            hasBlackQueenRookMoved = false;
        }

        // Check if move was castle and move rook back
        if (move.isCastleKingside) {
            if (s2.pieceColor == WHITE) {
                squares[7][5].movePiece(squares[7][7]);
            } else {
                squares[0][5].movePiece(squares[0][7]);
            }
        } else if (move.isCastleQueenside) {
            if (s2.pieceColor == WHITE) {
                squares[7][3].movePiece(squares[7][0]);
            } else {
                squares[0][3].movePiece(squares[0][0]);
            }
        }

        s2.movePiece(s1);
        if (move.isCapture) {
            s2.pieceID = move.capturedPieceValue;
            s2.pieceColor = move.capturedPieceColor;
        } else if (move.isEnPassant) {
            Square enPassantSquare = squares[s2.row - s1.pieceColor][s2.col];
            enPassantSquare.pieceID = 1;
            enPassantSquare.pieceColor = -s1.pieceColor;
        }
        if (move.isPromotion) {
            s1.pieceID = 1;
        }

        possibleEnPassant = move.previousEnPassantSquare;

        // TODO: undo hash
    }

    // Initializes board class and adds squares to square array.
    public Board() {
        squares = new Square[8][8];
        for (int row = 0; row < squares.length; row++) {
            for (int col = 0; col < squares.length; col++) {
                squares[row][col] = new Square(row, col);
            }
        }
    }

    // Starts a new game with pieces in their standard starting position.
    public void newGame() {
        turn = WHITE;
        plyNumber = 0;

        hasWhiteKingMoved = false;
        hasBlackKingMoved = false;
        hasWhiteKingRookMoved = false;
        hasWhiteQueenRookMoved = false;
        hasBlackKingRookMoved = false;
        hasBlackQueenRookMoved = false;
        possibleEnPassant = null;

        for (Square[] square : squares) {
            for (Square square1 : square) {
                square1.removePiece();
            }
        }

        squares[0][0].addPiece(4, 1);
        squares[0][1].addPiece(2, 1);
        squares[0][2].addPiece(3, 1);
        squares[0][3].addPiece(5, 1);
        squares[0][4].addPiece(6, 1);
        squares[0][5].addPiece(3, 1);
        squares[0][6].addPiece(2, 1);
        squares[0][7].addPiece(4, 1);
        squares[1][0].addPiece(1, 1);
        squares[1][1].addPiece(1, 1);
        squares[1][2].addPiece(1, 1);
        squares[1][3].addPiece(1, 1);
        squares[1][4].addPiece(1, 1);
        squares[1][5].addPiece(1, 1);
        squares[1][6].addPiece(1, 1);
        squares[1][7].addPiece(1, 1);
        squares[7][0].addPiece(4, -1);
        squares[7][1].addPiece(2, -1);
        squares[7][2].addPiece(3, -1);
        squares[7][3].addPiece(5, -1);
        squares[7][4].addPiece(6, -1);
        squares[7][5].addPiece(3, -1);
        squares[7][6].addPiece(2, -1);
        squares[7][7].addPiece(4, -1);
        squares[6][0].addPiece(1, -1);
        squares[6][1].addPiece(1, -1);
        squares[6][2].addPiece(1, -1);
        squares[6][3].addPiece(1, -1);
        squares[6][4].addPiece(1, -1);
        squares[6][5].addPiece(1, -1);
        squares[6][6].addPiece(1, -1);
        squares[6][7].addPiece(1, -1);

        hash = new ZobristHasher().getHash(this);
    }

    // Returns a new board which has the same properties as the original.
    public Board copy() {
        Board copy = new Board();
        copy.turn = getTurn();
        copy.plyNumber = plyNumber;

        copy.hasWhiteKingMoved = hasWhiteKingMoved;
        copy.hasBlackKingMoved = hasBlackKingMoved;
        copy.hasWhiteKingRookMoved = hasWhiteKingRookMoved;
        copy.hasWhiteQueenRookMoved = hasWhiteQueenRookMoved;
        copy.hasBlackKingRookMoved = hasBlackKingRookMoved;
        copy.hasBlackQueenRookMoved = hasBlackQueenRookMoved;
        copy.possibleEnPassant = possibleEnPassant;

        for (int row = 0; row < squares.length; row ++) {
            for (int col = 0; col < squares[row].length; col ++) {
                copy.squares[row][col] = squares[row][col].copy();
            }
        }

        return copy;
    }

    // returns board state if there are no valid moves on the board.
    public int isBoardCheckOrStaleMate() {
        boolean areLegalMoves = !getAllPossibleMoves().isEmpty();

        if (!areLegalMoves) {
            // Checks for checkmate
            if (isKingAttacked(getTurn())) {
                return getTurn() == WHITE ? 3 : 2;
            } else {
                // Checks for draw
                return DRAW;
            }
        }

        // Check for insufficient material

        // Check for pieces other than king
        // If pieces contains:
        // Nothing
        // Just bishop
        // Just knight
        // Just two knights
        boolean insufficientMaterial = true;
        ArrayList<Integer> pieces = new ArrayList<>();
        for (int color = -1; color <= 2; color += 2) {
            pieces.clear();
            for (Square[] row: squares) {
                for (Square square: row) {
                    if (square.pieceColor == color || square.pieceID != 6) {
                        pieces.add(square.pieceID);
                    }
                }
            }
            if (!pieces.isEmpty() && ((pieces.size() != 1 || (!pieces.contains(3) && !pieces.contains(2))) && (pieces.size() != 2 || !containsOnlyKnights(pieces)))) {
                insufficientMaterial = false;
            }
        }
        if (insufficientMaterial) {
            return DRAW;
        }
        return GAME_IN_PROGRESS;
    }

    // Returns all possible moves for a piece on the given square. Tries all moves to see if they will yield in an illegal position.
    public ArrayList<Move> getPossibleMoves(Square square) {
        if (square.pieceColor != turn) {
            return new ArrayList<>();
        } else {
            ArrayList<Move> possibleMoves = new ArrayList<>();
            for (Move move: getMoves(square)) {
                if (tryMove(move)) {
                    possibleMoves.add(move);
                }
            }
            return possibleMoves;
        }
    }

    // Checks if all pieces on the board are the same. Used for checking for 3 move repetition
    boolean equals(Board board) {
        for (int row = 0; row < squares.length; row ++) {
            for (int col = 0; col < squares[row].length; col ++) {
                if (!squares[row][col].equals(board.squares[row][col])) {
                    return false;
                }
            }
        }
        return true;
    }

    //////////////////////////////////////////////////

    // Creates a move given the 2 squares of the move and the new piece id (for promotion)
    private Move createMove(Square s1, Square s2) {
        Move newMove = new Move(s1.row, s1.col, s2.row, s2.col, s1.pieceID);
        if (s2.pieceID != 0) {
            newMove.isCapture = true;
            newMove.capturedPieceValue = s2.pieceID;
            newMove.capturedPieceColor = s2.pieceColor;
        }
        return newMove;
    }

    // Toggles the current turn.
    private void changeTurn() {
        turn = -turn;
    }

    // Returns if the kings OF the indicated color is attacked. This means that the square must be attacked by the OPPOSITE COLOR.
    private boolean isKingAttacked(int color) {
        //iterate through all squares
        for (Square[] square1 : squares) {
            for (Square square2 : square1) {
                if (square2.pieceID == 6 && square2.pieceColor == color && isSquareAttacked(square2, - color)) {
                    return true;
                }
            }
        }
        return false;
    }

    // Returns true if the square is being attacked by the designated color
    private boolean isSquareAttacked(Square square, int color) {
        // Check if attacked by pawn
        if (isLegalCoordinate(square.row + color)) {
            for (int colDirection = -1; colDirection <= 2; colDirection += 2) {
                if (isLegalCoordinate(square.col + colDirection) && isLegalCoordinate(square.row - color) ) {
                    Square attackSquare = squares[square.row - color][square.col + colDirection];
                    if (attackSquare.pieceID == 1 &&  attackSquare.pieceColor == color){
                        return true;
                    }
                }
            }
        }

        // Check if attacked by king
        for (int xDirection = -1; xDirection <= 1; xDirection ++) {
            for (int yDirection = -1; yDirection <= 1; yDirection ++) {
                int d = 1;
                int row = square.row + yDirection * d;
                int col = square.col + xDirection * d;
                if (isLegalCoordinate(row) && isLegalCoordinate(col)) {
                    Square attackSquare = squares[row][col];
                    if (attackSquare.pieceID == 6 && attackSquare.pieceColor == color) {
                        return true;
                    }
                }
            }
        }

        // Check if attacked by knight
        for (int xDirection = -1; xDirection <= 1; xDirection += 2) {
            for (int yDirection = -1; yDirection <= 1; yDirection += 2) {
                for (int p = 0; p <= 1; p++) {
                    int row = square.row + yDirection * (2 - p);
                    int col = square.col + xDirection * (1 + p);
                    if (isLegalCoordinate(row) && isLegalCoordinate(col)) {
                        Square attackSquare = squares[row][col];
                        if (attackSquare.pieceID == 2 && attackSquare.pieceColor == color) {
                            return true;
                        }
                    }
                }
            }
        }

        // Check if attacked by bishop/queen
        for (int xDirection = -1; xDirection <= 1; xDirection += 2) {
            for (int yDirection = -1; yDirection <= 1; yDirection += 2) {
                for (int d = 1; d < 8; d++) {
                    int row = square.row + yDirection * d;
                    int col = square.col + xDirection * d;
                    if (isLegalCoordinate(row) && isLegalCoordinate(col)){
                        Square attackSquare = squares[row][col];
                        if (attackSquare.pieceColor == color && (attackSquare.pieceID == 3 || attackSquare.pieceID == 5)) {
                            return true;
                        } else if (attackSquare.pieceColor != 0) {
                            break;
                        }
                    } else {
                        break;
                    }
                }
            }
        }

        // Check if attacked by rook/queen
        for (int direction = 0; direction <= 1; direction ++) {
            for (int magnitude = -1; magnitude <= 1; magnitude += 2) {
                for (int n = 1; n < 8; n++) {
                    int row = square.row + direction * magnitude * n;
                    int col = square.col + (1 - direction) * magnitude * n;
                    if (isLegalCoordinate(row) && isLegalCoordinate(col) && squares[row][col].pieceColor != square.pieceColor){
                        Square attackSquare = squares[row][col];
                        if (attackSquare.pieceColor == color && (attackSquare.pieceID == 4 || attackSquare.pieceID == 5)) {
                            return true;
                        } else if (attackSquare.pieceColor != 0) {
                            break;
                        }
                    } else {
                        break;
                    }
                }
            }
        }
        return false;
    }

    // Returns true if move results in a legal position
    private boolean tryMove(Move move) {
        movePiece(move);
        boolean isPossibleMove = !isKingAttacked(-turn);
        reverseMove(move);
        return isPossibleMove;
    }

    // Returns if n is a row or col on the board
    public static boolean isLegalCoordinate(int n) {
        return n >= 0 && n < 8;
    }

    // Gets all possible moves for the piece on the given square. Adds moves for pawn that weren't attacks.
    public ArrayList<Move> getMoves(Square square) {
        ArrayList<Move> possibleMoves = getAttacks(square);
        int iD = square.pieceID;
        int color = square.pieceColor;

        // Add non attack pawn moves
        if (iD == 1) {
            if (isLegalCoordinate(square.row + color)) {
                if (!squares[square.row + color][square.col].containsPiece()) {
                    if (square.row == (int) (2.5 * color + 3.5) && !squares[square.row + color][square.col].containsPiece()) {
                        for (int newPieceID = 2; newPieceID <= 5; newPieceID ++) {
                            Move promotion = createMove(square, squares[square.row + color][square.col]);
                            promotion.isPromotion = true;
                            promotion.endPieceValue = newPieceID;
                            possibleMoves.add(promotion);
                        }
                    } else {
                        possibleMoves.add(createMove(square, squares[square.row + color][square.col]));
                        if (square.row == (int) (-2.5 * color + 3.5) && !squares[square.row + 2 * color][square.col].containsPiece()) {
                            Move doublePawnMove = createMove(square, squares[square.row + 2 * color][square.col]);
                            doublePawnMove.newEnPassantSquare = squares[square.row + color][square.col];
                            possibleMoves.add(doublePawnMove);
                        }
                    }
                }
            }
        }

        ArrayList<Move> possibleMovesWithoutPawnAttacks = new ArrayList<>();
        for (Move move: possibleMoves) {
            if (square.pieceID != 1 || move.endCol == square.col || squares[move.endRow][move.endCol].pieceID != 0) {
                possibleMovesWithoutPawnAttacks.add(move);
            } else if (squares[move.endRow][move.endCol] == possibleEnPassant && (squares[move.startRow][move.startCol].pieceColor == WHITE && move.endRow == 2||squares[move.startRow][move.startCol].pieceColor == BLACK && move.endRow == 5)) {
                move.isEnPassant = true;
                possibleMovesWithoutPawnAttacks.add(move);
            }
        }

        // Castling
        if (square.pieceID == 6) {

            ///////////////////////////////////////

            if (square.pieceColor == WHITE && !hasWhiteKingMoved) {
                if (!hasWhiteKingRookMoved) {
                    if (!isSquareAttacked(squares[7][4], BLACK) && !isSquareAttacked(squares[7][5], BLACK) && !isSquareAttacked(squares[7][6], BLACK) && !squares[7][5].containsPiece() && !squares[7][6].containsPiece()) {
                        Move move = createMove(square, squares[7][6]);
                        move.isCastleKingside = true;
                        possibleMovesWithoutPawnAttacks.add(move);
                    }
                }
                if (!hasWhiteQueenRookMoved) {
                    if (!isSquareAttacked(squares[7][1], BLACK) && !isSquareAttacked(squares[7][2], BLACK) && !isSquareAttacked(squares[7][3], BLACK) && !isSquareAttacked(squares[7][4], BLACK) && !squares[7][1].containsPiece() && !squares[7][2].containsPiece() && !squares[7][3].containsPiece()) {
                        Move move = createMove(square, squares[7][2]);
                        move.isCastleQueenside = true;
                        possibleMovesWithoutPawnAttacks.add(move);
                    }
                }
            } else if (square.pieceColor == BLACK && !hasBlackKingMoved) {


                if (!hasBlackKingRookMoved) {

                    if (!isSquareAttacked(squares[0][4], WHITE) && !isSquareAttacked(squares[0][5], WHITE) && !isSquareAttacked(squares[0][6], WHITE) && !squares[0][5].containsPiece() && !squares[0][6].containsPiece()) {
                        Move move = createMove(square, squares[0][6]);
                        move.isCastleKingside = true;
                        possibleMovesWithoutPawnAttacks.add(move);
                    }
                }
                if (!hasBlackQueenRookMoved) {
                    if (!isSquareAttacked(squares[0][1], WHITE) && !isSquareAttacked(squares[0][2], WHITE) && !isSquareAttacked(squares[0][3], WHITE) && !isSquareAttacked(squares[0][4], WHITE) && !squares[0][1].containsPiece() && !squares[0][2].containsPiece() && !squares[0][3].containsPiece()) {
                        Move move = createMove(square, squares[0][2]);
                        move.isCastleQueenside = true;
                        possibleMovesWithoutPawnAttacks.add(move);
                    }
                }
            }

            ///////////////////////////////////////

        }

        for (Move move: possibleMovesWithoutPawnAttacks) {
            move.previousEnPassantSquare = possibleEnPassant;

            if (move.startRow == 0 && move.startCol == 0 && !hasBlackQueenRookMoved) {
                move.isFirstBlackQueenRookMove = true;
            } else if (move.startRow == 0 && move.startCol == 4 && !hasBlackKingMoved) {
                move.isFirstBlackKingMove = true;
            } else if (move.startRow == 0 && move.startCol == 7 && !hasBlackKingRookMoved) {
                move.isFirstBlackKingRookMove = true;
            } else if (move.startRow == 7 && move.startCol == 0 && !hasWhiteQueenRookMoved) {
                move.isFirstWhiteQueenRookMove = true;
            } else if (move.startRow == 7 && move.startCol == 4 && !hasWhiteKingMoved) {
                move.isFirstWhiteKingMove = true;
            } else if (move.startRow == 7 && move.startCol == 7 && !hasWhiteKingRookMoved) {
                move.isFirstWhiteKingRookMove = true;
            }
        }

        return possibleMovesWithoutPawnAttacks;
    }

    // Gets all possible attacks for a piece on the given square.
    private ArrayList<Move> getAttacks(Square square) {
        ArrayList<Move> possibleAttacks = new ArrayList<>();
        int iD = square.pieceID;
        int color = square.pieceColor;
        if (iD == 1) {
            if (isLegalCoordinate(square.row + color)) {
                for (int direction = -1; direction <= 1; direction += 2) {
                    if (isLegalCoordinate(square.col + direction) && (squares[square.row + color][square.col + direction].pieceColor != square.pieceColor || (possibleEnPassant != null && square.row == possibleEnPassant.row && square.col == possibleEnPassant.col))) {
                        if (square.row + color == 0 || square.row + color == 7) {
                            for (int newPieceID = 2; newPieceID <= 5; newPieceID ++) {
                                Move promotion = createMove(square, squares[square.row + color][square.col + direction]);
                                promotion.isPromotion = true;
                                promotion.endPieceValue = newPieceID;
                                possibleAttacks.add(promotion);
                            }
                        } else {
                            possibleAttacks.add(createMove(square, squares[square.row + color][square.col + direction]));
                        }
                    }
                }
            }
        } else if (iD == 2) {
            for (int xDirection = -1; xDirection <= 1; xDirection += 2) {
                for (int yDirection = -1; yDirection <= 1; yDirection += 2) {
                    for (int p = 0; p <= 1; p++) {
                        int row = square.row + yDirection * (2 - p);
                        int col = square.col + xDirection * (1 + p);
                        if (isLegalCoordinate(row) && isLegalCoordinate(col) && squares[row][col].pieceColor != square.pieceColor){ //
                            possibleAttacks.add(createMove(square, squares[row][col]));
                        }
                    }
                }
            }
        } else if (iD == 3) {
            for (int xDirection = -1; xDirection <= 1; xDirection += 2) {
                for (int yDirection = -1; yDirection <= 1; yDirection += 2) {
                    for (int d = 1; d < 8; d++) {
                        int row = square.row + yDirection * d;
                        int col = square.col + xDirection * d;
                        if (isLegalCoordinate(row) && isLegalCoordinate(col) && squares[row][col].pieceColor != square.pieceColor){
                            possibleAttacks.add(createMove(square, squares[row][col]));
                            if (squares[row][col].pieceColor != 0) {
                                break;
                            }
                        } else {
                            break;
                        }
                    }
                }
            }
        } else if (iD == 4) {
            for (int direction = 0; direction <= 1; direction ++) {
                for (int magnitude = -1; magnitude <= 1; magnitude += 2) {
                    for (int n = 1; n < 8; n++) {
                        int row = square.row + direction * magnitude * n;
                        int col = square.col + (1 - direction) * magnitude * n;
                        if (isLegalCoordinate(row) && isLegalCoordinate(col) && squares[row][col].pieceColor != square.pieceColor){
                            possibleAttacks.add(createMove(square, squares[row][col]));
                            if (squares[row][col].pieceColor != 0) {
                                break;
                            }
                        } else {
                            break;
                        }
                    }
                }
            }
        } else if (iD == 5) {
            for (int xDirection = -1; xDirection <= 1; xDirection ++) {
                for (int yDirection = -1; yDirection <= 1; yDirection ++) {
                    for (int d = 1; d < 8; d++) {
                        int row = square.row + yDirection * d;
                        int col = square.col + xDirection * d;
                        if (isLegalCoordinate(row) && isLegalCoordinate(col) && squares[row][col].pieceColor != square.pieceColor){
                            possibleAttacks.add(createMove(square, squares[row][col]));
                            if (squares[row][col].pieceColor != 0) {
                                break;
                            }
                        } else {
                            break;
                        }
                    }
                }
            }
        } else if (iD == 6) {
            for (int xDirection = -1; xDirection <= 1; xDirection ++) {
                for (int yDirection = -1; yDirection <= 1; yDirection ++) {
                    int d = 1;
                    int row = square.row + yDirection * d;
                    int col = square.col + xDirection * d;
                    if (isLegalCoordinate(row) && isLegalCoordinate(col) && square.pieceColor != squares[row][col].pieceColor){
                        Move move = createMove(square, squares[row][col]);
                        possibleAttacks.add(move);
                    }
                }
            }
        }

        return possibleAttacks;
    }

    // Returns true if a list contains only knights
    private boolean containsOnlyKnights(ArrayList<Integer> list) {
        for (Integer item: list) {
            if (!item.equals(2)) {
                return false;
            }
        }
        return true;
    }

    // Adds a piece to a square
    void addPiece(int row, int col, int pieceColor, int pieceID) {
        squares[row][col].addPiece(pieceID, pieceColor);
    }

    // Get ready to start a new game
    void primeGame() {
        turn = WHITE;
        plyNumber = 0;

        hasWhiteKingMoved = false;
        hasBlackKingMoved = false;
        hasWhiteKingRookMoved = false;
        hasWhiteQueenRookMoved = false;
        hasBlackKingRookMoved = false;
        hasBlackQueenRookMoved = false;
        possibleEnPassant = null;

        for (Square[] square : squares) {
            for (Square square1 : square) {
                square1.removePiece();
            }
        }
    }

    void setTurn(int turn) {
        this.turn = turn;
    }

    void setPlyNumber(int plyNumber) {
        this.plyNumber = plyNumber;
    }

    // void updateHash(Move move) {}

    long getHash () {
        hash = zobristHasher.getHash(this);
        return hash;
    }

    boolean whiteCastleKingside() {
        return (!hasWhiteKingRookMoved) && (!hasWhiteKingMoved);
    }

    boolean whiteCastleQueenside() {
        return (!hasWhiteQueenRookMoved) && (!hasWhiteKingMoved);
    }

    boolean blackCastleKingside() {
        return (!hasBlackKingRookMoved) && (!hasBlackKingMoved);
    }

    boolean blackCastleQueenside() {
        return (!hasBlackQueenRookMoved) && (!hasBlackKingMoved);
    }

    boolean hasEnPassant() {
        if (possibleEnPassant != null) {
            boolean hasPossibleEnPassant = false;
            if (possibleEnPassant.col - 1 >= 0) {
                Square possibleSquare1 = squares[possibleEnPassant.row + turn][possibleEnPassant.col - 1];
                if (possibleSquare1.pieceID == 1 && possibleSquare1.pieceColor == turn) {
                    hasPossibleEnPassant = true;
                }
            }
            if (possibleEnPassant.col + 1 < 8) {
                Square possibleSquare2 = squares[possibleEnPassant.row + turn][possibleEnPassant.col + 1];
                if (possibleSquare2.pieceID == 1 && possibleSquare2.pieceColor == turn) {
                    hasPossibleEnPassant = true;
                }
            }
            return hasPossibleEnPassant;
        } else {
            return false;
        }
    }

    Square enPassantSquare() {
        return possibleEnPassant;
    }

    public Move createMove(String uciMove) {

        int startRow = reverseRowNames.get(uciMove.substring(1, 2));
        int startCol = reverseColNames.get(uciMove.substring(0, 1));
        int endRow = reverseRowNames.get(uciMove.substring(3, 4));
        int endCol = reverseColNames.get(uciMove.substring(2, 3));

        int pieceValue = squares[startRow][startCol].pieceID;
        int pieceColor = squares[startRow][startCol].pieceColor;

        // Check for promotion


        Move move = new Move(startRow, startCol, endRow, endCol, pieceValue);


       if ((pieceValue == 1) && (pieceColor == BLACK && endRow == 7) || (pieceColor == WHITE && endRow == 0)) {
           move.isPromotion = true;
           move.endPieceValue = 5;
       }

        //Check for castling
        if (pieceValue == 6) {
            if (Math.abs(startCol - endCol) == 2) {
                move.isCastleKingside = true;
            }
            if (Math.abs(startCol - endCol) == 3) {
                move.isCastleQueenside = true;
            }
        }

        if (squares[endRow][endCol].pieceID != 0) {
            move.isCapture = true;
            move.capturedPieceValue = squares[endRow][endCol].pieceID;
            move.capturedPieceColor = squares[endRow][endCol].pieceColor;
        }

        // TODO: En passant

        if (move.pieceValue == 1 && move.startCol - move.endCol != 0 && !move.isCapture && squares[move.endRow][move.endCol].pieceID == 0) {
            System.out.println("ENPASSANT PLAYED");
            move.isEnPassant = true;
            move.isCapture = true;
        }

        if (move.startRow == 0 && move.startCol == 0 && !hasBlackQueenRookMoved) {
            move.isFirstBlackQueenRookMove = true;
        } else if (move.startRow == 0 && move.startCol == 4 && !hasBlackKingMoved) {
            move.isFirstBlackKingMove = true;
        } else if (move.startRow == 0 && move.startCol == 7 && !hasBlackKingRookMoved) {
            move.isFirstBlackKingRookMove = true;
        } else if (move.startRow == 7 && move.startCol == 0 && !hasWhiteQueenRookMoved) {
            move.isFirstWhiteQueenRookMove = true;
        } else if (move.startRow == 7 && move.startCol == 4 && !hasWhiteKingMoved) {
            move.isFirstWhiteKingMove = true;
        } else if (move.startRow == 7 && move.startCol == 7 && !hasWhiteKingRookMoved) {
            move.isFirstWhiteKingRookMove = true;
        }

        return move;

    }

    public String getUCI(Move move) {
        String s1 = Move.colConversions.get(move.startCol) + Move.rowConversions.get(move.startRow);
        String s2 = Move.colConversions.get(move.endCol) + Move.rowConversions.get(move.endRow);
        return s1 + s2;
    }

    public void printBoard() {
        for (Square[] row: squares) {
            for (Square square: row) {
                if (square.containsPiece()) {
                    if (square.pieceID == 1) {
                        System.out.print("p ");
                    } else {
                        System.out.print(Move.pieceConversions.get(square.pieceID) + " ");
                    }
                } else {
                    System.out.print("_ ");
                }
            }
            System.out.println();
        }
    }


    public void toggleTurn() {
        turn = -turn;
    }

}
