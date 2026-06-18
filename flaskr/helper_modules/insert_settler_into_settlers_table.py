from .. import db

def insert_settler_into_settlers_table(username, settler_id):
    
    database_connection =  db.get_db()

    database_connection.execute("""INSERT INTO 'settlers' (id, username) VALUES (?, ?)""", (settler_id, username,))

    database_connection.commit()

    return