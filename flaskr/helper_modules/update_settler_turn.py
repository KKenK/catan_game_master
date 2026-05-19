from .. import db

def update_settler_turn(settler_turn):
    
    database_connection = db.get_db()
    
    database_connection.execute("""UPDATE 'game_progress' SET (settler_turn) = (?)""", (settler_turn,))

    database_connection.commit()