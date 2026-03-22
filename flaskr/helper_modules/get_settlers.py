def get_settlers(database_connector):
    with database_connector() as db:
        return db.execute("""SELECT * FROM settlers""")
    
def get_first_settler_without_settlement(database_connector):
    with database_connector() as db:
        return db.execute("""SELECT * FROM settlers WHERE victory_points = 0 LIMIT 1""").fetchone()

def get_last_settler_without_city(database_connector):
    with database_connector() as db:
        return db.execute("""SELECT * FROM settlers WHERE victory_points = 1 ORDER BY id DESC LIMIT 1""")