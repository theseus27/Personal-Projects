import berserk
import move
import threading
import vfx
import board

WAIT_TIME = 10
LOG_FILE = "log2.txt"

class GameState:
    def __init__(self, game, session):
        self.game = game
        self.id = game["gameId"]

        self.b = board.Board()

        self.generator = berserk.clients.Board(session).stream_game_state(self.id)
        self.initial_state = next(self.generator)
        self.curr_state = self.initial_state
        self.write_state(self.initial_state)
        self.moves = self.parse_moves(self.initial_state["state"]["moves"])

        self.status = game["status"]["name"]
        self.board = berserk.clients.Board(session)
    
    def display_board(self):
        vfx.display_board(self.b)


    def write_state(self, state):
        with open(LOG_FILE, 'a') as log:
            log.write(str(state))
            log.write("\n\n")
    
    def parse_moves(self, moves):
        move_list = []
        move_strs = moves.strip().split()

        for move_str in move_strs:
            move_list.append(move.Move(move_str))
            self.b.make_move(move_str)
        return move_list

    def print_all_moves(self):
        for m in self.moves:
            print(m.as_string(True))
    
    def get_move_num(self, num):
        if num <= len(self.moves):
            return self.moves[num-1].as_string()
        else:
            print("Invalid move number " + str(num) + ". There have currently been " + str(len(self.moves) + " moves"))

    def num_moves_played(self):
        return len(self.moves)
    
    def update_moves(self, new_move_str):
        last_move_str = self.moves[-1].as_string()
        if last_move_str == new_move_str:
            raise Exception("Failed to update moves")
        else:
            self.moves.append(move.Move(new_move_str))
            self.b.make_move(new_move_str)

    def get_next_user_move(self):
        valid_move = False
        while not valid_move:
            m = input("Enter a move in the format [startsquare][endsquare] (ex. 'e2e4') ")
            try:
                self.board.make_move(self.id, m)
                valid_move = True
            except:
                print("Invalid move " + str(m))
    
        next_state = next(self.generator)
        self.write_state(next_state)
        self.curr_state = next_state
        next_state_moves = next_state["moves"].strip().split()
        new_move_str = next_state_moves[-1]
        self.update_moves(new_move_str)

        self.status = next_state["status"]
            

    def next_comp_helper(self, e, res_dic):
        next_state = None
        next_state = next(self.generator)
        if next_state is not None:
            e.set()
            res_dic['res'] = next_state

    def get_next_computer_move(self):
        comp_move = {'res': None}
        new_state = None

        e = threading.Event()
        t = threading.Thread(target=self.next_comp_helper, args=(e, comp_move))
        t.start()
        t.join(WAIT_TIME)
        if t.is_alive():
            e.set()
        else:
            new_state = comp_move['res']
        
        if new_state != None:
            self.write_state(new_state)
            self.curr_state = new_state
            new_state_moves = new_state["moves"].strip().split()
            new_move_str = new_state_moves[-1]
            self.update_moves(new_move_str)
        else:
            print("Failed to get next computer move, thread time out")

    def is_over(self):
        if self.status != "started":
            return True
        return False
