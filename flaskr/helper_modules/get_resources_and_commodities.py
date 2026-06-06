from .. import db

def get_resources_and_commodities():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT id, resources.name, city_resources_commodities.name FROM resources LEFT JOIN city_resources_commodities USING(id)""").fetchall()
    