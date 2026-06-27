from .. import db

def get_game_progress_data():
    
    database_connection = db.get_db()

    return database_connection.execute("""SELECT * FROM game_progress""").fetchone()