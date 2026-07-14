from .. import db

def remove_first_settler_from_settlers_that_contributed_least_to_catans_defence_table(settler_id):
    
    database_connection = db.get_db()
    
    database_connection.execute("""DELETE FROM 'settlers_that_contributed_least_to_catans_defence' WHERE id = (?)""", (settler_id,))

    database_connection.commit()