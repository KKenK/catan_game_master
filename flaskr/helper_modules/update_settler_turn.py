from .. import db

def update_settler_turn(settler_turn, is_settler_two):
    
    database_connection = db.get_db()
    
    database_connection.execute("""UPDATE 'game_progress' SET (settler_turn, is_settler_two) = (?,?)""", (settler_turn, is_settler_two))

    database_connection.commit()