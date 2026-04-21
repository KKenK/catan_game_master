from .. import db

def update_game_progress(game_status):
    
    database_connection = db.get_db()
    
    database_connection.execute("""UPDATE INTO 'game_progress' (progress) VALUES (?)""", (game_status,))