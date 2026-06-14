from .. import db

def activate_knight(knight_id):

    database_connection = db.get_db()
    
    database_connection.execute("""UPDATE knights SET is_active = 1 where id = ?""", (knight_id,))

    database_connection.commit()

    return
