from .. import db

def update_dice_roll(red, white, event):

    database_connection =  db.get_db()

    database_connection.execute("""UPDATE 'dice_roll' SET (red, white, event) = (?, ?, ?)""", (red, white, event))

    database_connection.commit()

    return