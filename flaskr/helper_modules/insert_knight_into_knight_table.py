from .. import db

def insert_knight(settler_id, knight_id):

    database_connection = db.get_db()

    database_connection.execute("""INSERT INTO knights (id, settler_id, level) VALUES (?,?,?)""", (knight_id, settler_id, 1))

    database_connection.commit()

    return