from .. import db

def assign_has_longest_road(settler_id):

    database_connection = db.get_db()

    database_connection.execute("""UPDATE settlers SET has_longest_road = 1 WHERE id = (?)""", (settler_id,))

    database_connection.commit()

    return
