import berserk

def create_new_game(session, level=1):
    game = berserk.clients.Challenges(session).create_ai(level)
    return game

def fetch_game_by_id(session, id):
    games = berserk.clients.Games(session).get_ongoing()
    for game in games:
        if game["gameId"] == id:
            return game
    return None

def list_ids(session):
    games = berserk.clients.Games(session).get_ongoing()
    for game in games:
        print(game["gameId"])