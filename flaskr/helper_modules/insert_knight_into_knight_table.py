from .. import db
from . import calculate_row_id

def insert_knight(settler_id):

    knight_id = calculate_row_id.calculate_row_id("knights")

    database_connection = db.get_db()
    print((knight_id, settler_id, 1))
    database_connection.execute("""INSERT INTO knights (id, settler_id, level) VALUES (?,?,?)""", (knight_id, settler_id, 1))

    database_connection.commit()

    return