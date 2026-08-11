from .. import db

def increment_victory_point_card_count(settler_id, increment_value = 1):

    database_connection = db.get_db()

    database_connection.execute("""UPDATE settlers SET victory_point_card = victory_point_card + (?) WHERE id = (?)""", (increment_value, settler_id,))

    database_connection.commit()

    return