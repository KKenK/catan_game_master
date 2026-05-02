from .. import db

def update_game_progress(game_status):
    
    database_connection = db.get_db()
    
    database_connection.execute("""UPDATE 'game_progress' SET (progress) VALUES (?)""", (game_status,))

    database_connection.commit()