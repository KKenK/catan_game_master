from .. import db

def populate_dice_roll(red, white, event):

    database_connection =  db.get_db()

    database_connection.execute("""INSERT INTO 'dice_roll' (red, white, event) VALUES (?, ?, ?)""", (red, white, event))

    database_connection.commit()

    return