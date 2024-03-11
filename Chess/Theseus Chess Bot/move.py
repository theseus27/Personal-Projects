import berserk

class Move:
    TOTAL_MOVES = 0

    def __init__(self, movestr):
        self.stringified = movestr
        self.old = movestr[0:2]
        self.new = movestr[2:4]
        self.capture = False

        self.number = Move.TOTAL_MOVES + 1
        Move.TOTAL_MOVES += 1

        self.side = ""
        if self.number % 2 == 0:
            self.side = "black"
        else:
            self.side = "white"
    
    def as_string(self, verbose=False):
        if verbose:
            move_str = "Move " + str(self.number) + " (" + str(self.side) + "): " + str(self.old) + " to " + str(self.new)
            if self.capture:
                move_str += " (capture)"
            return move_str
        else:
            return self.stringified
        
    def get_num(self):
        return self.number