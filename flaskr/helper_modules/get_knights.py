from .. import db

def get_knights():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM knights""").fetchall()
