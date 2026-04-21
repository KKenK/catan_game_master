from .. import db

def get_game_progress():
    
    database_connection = db.get_db()

    return database_connection.execute("""SELECT 'progress' FROM game_progress""").fetchone()
  