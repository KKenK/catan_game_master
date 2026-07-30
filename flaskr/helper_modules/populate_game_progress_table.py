from .. import db

def populate_game_progress_table():
    
    database_connection =  db.get_db()

    database_connection.execute("""INSERT INTO 'game_progress' (progress) VALUES ('uninitialised')""")

    database_connection.commit()

    return