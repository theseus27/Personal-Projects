class Board:
    def __init__(self):
        self.captured = []
        self.squares = [["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
                        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                        ["", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", ""],
                        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]]
        
    def make_move(self, move):
        from_file = ord(move[0].lower()) - 97  
        from_rank = int(move[1]) - 1
        to_file = ord(move[2].lower()) - 97
        to_rank = int(move[3]) - 1

        capture = False
        if self.squares[to_file][to_rank] != "":
            capture = True
            self.captured.append(self.squares[to_file][to_rank])
            self.squares[to_file][to_rank] = self.squares[from_file][from_rank]
            self.squares[from_file][from_rank] = ""
        
        return capture