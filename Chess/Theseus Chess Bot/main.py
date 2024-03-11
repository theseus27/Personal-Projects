import os
import dotenv
import berserk
import game_mod
from game_state import GameState

dotenv.load_dotenv()

session = berserk.TokenSession(os.getenv("API_TOKEN"))
client = berserk.Client(session=session)

game = None
game_id = ""

while game is None:
    game_id = input("Enter game id or press enter to create new game\nType 'list ids' to see a list of current ids\n\n")
    if game_id == "":
        game = game_mod.create_new_game(session)
        game_id = game["id"]
        game = game_mod.fetch_game_by_id(session, game_id)
    elif game_id == "list ids":
        game_mod.list_ids(session)
    else:
        game = game_mod.fetch_game_by_id(session, game_id)
        if game is None:
            print("Error fetching game " + str(game_id))
        game_id = game["gameId"]

state = GameState(game, session)

user_side = game['color']
os.system('cls')
print("You are " + str(user_side) + "\n")

state.print_all_moves()

while not state.is_over():
    state.get_next_user_move()

    if state.is_over():
        break

    state.get_next_computer_move()
    comp_move = state.moves[-1]
    state.display_board()
    print("\nThe computer played " + str(comp_move.old) + " to " + str(comp_move.new))

end_state = state.curr_state
print("\nGame over\n" + str(end_state["winner"].capitalize()) + " wins!")