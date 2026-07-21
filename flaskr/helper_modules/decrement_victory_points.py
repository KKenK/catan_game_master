from .. import db

def decrement_victory_points(settler_id, increment_value = -1):

    database_connection = db.get_db()

    database_connection.execute("""UPDATE settlers SET victory_points = victory_points - (?) WHERE id = (?)""", (increment_value, settler_id,))

    database_connection.commit()

    return