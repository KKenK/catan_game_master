from .. import db

def get_metropolises():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM metropolises""").fetchall()

def get_metropolis_via_city_improvement(city_improvement):
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM metropolises WHERE city_improvement = ?""",(city_improvement,)).fetchone()



    