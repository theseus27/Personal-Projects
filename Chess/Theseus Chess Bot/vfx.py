import enum

class Color(enum.Enum):
    WHITE = 0
    BLACK = 1

class Piece(enum.Enum):
    EMPTY = enum.auto()
    PAWN = enum.auto()
    ROOK = enum.auto()
    KNIGHT = enum.auto()
    BISHOP = enum.auto()
    KING = enum.auto()
    QUEEN = enum.auto()

CHRS = {
    (Color.WHITE, Piece.EMPTY): "\u25FB",
    (Color.WHITE, Piece.PAWN): "\u265F",
    (Color.WHITE, Piece.ROOK): "\u265C",
    (Color.WHITE, Piece.KNIGHT): "\u265E",
    (Color.WHITE, Piece.BISHOP): "\u265D",
    (Color.WHITE, Piece.KING): "\u265A",
    (Color.WHITE, Piece.QUEEN): "\u265B",
    (Color.BLACK, Piece.EMPTY): "\u25FC",
    (Color.BLACK, Piece.PAWN): "\u2659",
    (Color.BLACK, Piece.ROOK): "\u2656",
    (Color.BLACK, Piece.KNIGHT): "\u2658",
    (Color.BLACK, Piece.BISHOP): "\u2657",
    (Color.BLACK, Piece.KING): "\u2654",
    (Color.BLACK, Piece.QUEEN): "\u2655",
}

def process_piece_at_square(piece, square):
    color = None
    piece_type = None

    if piece == "":
        piece_type = Piece.EMPTY
        # TODO: Figure out if it should be white or black
        rank, file = square[0], square[1]
        if file % 2 == 0:
            color = Color.BLACK if rank % 2 == 0 else Color.WHITE
        elif file % 2 == 1:
            color = Color.WHITE if rank % 2 == 0 else Color.BLACK

    else:
        if piece[0] == 'w':
            color = Color.WHITE
        else:
            color = Color.BLACK
        
        if piece[1] == 'R':
            piece_type = Piece.ROOK
        elif piece[1] == 'N':
            piece_type = Piece.KNIGHT
        elif piece[1] == 'B':
            piece_type = Piece.BISHOP
        elif piece[1] == 'Q':
            piece_type = Piece.QUEEN
        elif piece[1] == 'K':
            piece_type = Piece.KING
        elif piece[1] == 'P':
            piece_type = Piece.PAWN
        else:
            print("ERROR " + str(piece))
        
    return CHRS[(color, piece_type)]


def display_board(board):
    print("\n")
    for rank in range(8):
        rank_strs = []
        for file in range(8):
            rank_strs.append(process_piece_at_square(board.squares[rank][file], [rank, file]))
        print("".join(rank_strs))
    print("\n")