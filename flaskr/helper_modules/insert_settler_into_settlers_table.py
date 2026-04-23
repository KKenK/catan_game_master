from .. import db

def insert_settler_into_settlers_table( username):
    
    return db.get_db().execute("""INSERT INTO 'settlers' (username) VALUES (?) RETURNING id""", (username,)).fetchone()[0]