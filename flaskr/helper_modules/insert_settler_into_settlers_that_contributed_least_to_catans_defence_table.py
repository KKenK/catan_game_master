from .. import db

def insert_settler_into_settlers_that_contributed_least_to_catans_defence_table(settler_ids):
    
    database_connection =  db.get_db()

    for settler_id in settler_ids:
    
        database_connection.execute("""INSERT INTO 'settlers_that_contributed_least_to_catans_defence' (id) VALUES (?)""", (settler_id,))

    database_connection.commit()

    return