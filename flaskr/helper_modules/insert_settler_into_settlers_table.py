from .. import db
from . import calculate_row_id

def insert_settler_into_settlers_table(username):
    
    database_connection =  db.get_db()

    settler_id = calculate_row_id.calculate_row_id("settlers")

    database_connection.execute("""INSERT INTO 'settlers' (id, username) VALUES (?, ?)""", (settler_id, username,))

    database_connection.commit()

    return settler_id