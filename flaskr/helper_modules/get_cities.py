from .. import db

def get_cities():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM settlements WHERE is_city = 1""").fetchall()