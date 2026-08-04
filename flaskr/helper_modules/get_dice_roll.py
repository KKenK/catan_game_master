from .. import db

def get_dice_roll():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM dice_roll""").fetchone()
