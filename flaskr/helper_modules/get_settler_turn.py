from .. import db

def get():

    database_connection = db.get_db()

    return database_connection.execute("""SELECT "settler_turn" FROM game_progress""").fetchone()