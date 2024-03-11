import berserk

API_TOKEN = "lip_Uvmcg05EwH4ZWCxMHSkb"
GAME_ID = ""

session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)

# board = berserk.clients.Board(session)
game = berserk.clients.Challenges(session).create_ai(level=1)


# games = client.games.get_ongoing()
# print(games)