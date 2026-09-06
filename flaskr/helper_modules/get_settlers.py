from .. import db

def get_settlers():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM settlers ORDER BY id""").fetchall()
    
def get_first_settler_without_settlement():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM settlers WHERE victory_points = 0 LIMIT 1""").fetchone()

def get_last_settler_without_city():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM settlers WHERE victory_points = 1 ORDER BY id DESC LIMIT 1""").fetchone()

def get_settler_via_id(settler_id):

    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM settlers WHERE id = ?""", (settler_id,)).fetchone()
   