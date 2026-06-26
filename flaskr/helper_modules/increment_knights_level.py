from .. import db

def increment_knights_level(knight_id_tuple, increment_value = 1):

    database_connection = db.get_db()

    for knight_id in knight_id_tuple:

        database_connection.execute("""UPDATE knights SET level = level + (?) WHERE id = (?)""", (increment_value, knight_id,))

    database_connection.commit()

    return