from .. import db

def insert_settler_into_settlers_table(username):
    
    database_connection =  db.get_db()

    database_connection.execute("""INSERT INTO 'settlers' (username) VALUES (?) RETURNING id""", (username,)).fetchone()[0]

    database_connection.commit()

    return