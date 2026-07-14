from .. import db

def get_settlers_that_contributed_least_to_catans_defence():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM settlers_that_contributed_least_to_catans_defence""").fetchall()
    