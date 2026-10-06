from .. import db

def increment_city_improvement(settler_id, city_improvement):

    database_connection = db.get_db()

    if city_improvement == "trade":
        database_connection.execute("""UPDATE settlers SET trade = trade + 1 WHERE id = (?)""", (settler_id,))
    
    elif city_improvement == "politics":
        database_connection.execute("""UPDATE settlers SET politics = politics + 1 WHERE id = (?)""", (settler_id,))
    
    elif city_improvement == "science":
        database_connection.execute("""UPDATE settlers SET science = science + 1 WHERE id = (?)""", (settler_id,))

    database_connection.commit()

    return