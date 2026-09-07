from .. import db

def increment_victory_points_cards(settler_id):

    database_connection = db.get_db()

    database_connection.execute("""UPDATE settlers SET victory_point_cards = victory_point_cards + 1 WHERE id = (?)""", (settler_id,))

    database_connection.commit()

    return