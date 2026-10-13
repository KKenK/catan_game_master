from .. import db

def metropolis_settler_id(city_improvement, settler_id):
    
    database_connection = db.get_db()

    database_connection.execute("""UPDATE metropolises SET settler_id = ? WHERE city_improvement = ?""", (settler_id, city_improvement))

    database_connection.commit()

    return

def increment_metropolis_level(city_improvement):
        
    database_connection = db.get_db()

    database_connection.execute("""UPDATE metropolises SET level = level + 1 WHERE city_improvement = ?""", (settler_id, city_improvement))

    database_connection.commit()

    return