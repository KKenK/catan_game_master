from .. import db

def set_resources_table(resource_tuple_list):
    
    database_connection = db.get_db()
    
    database_connection.executemany("""INSERT INTO 'resources' (id, name) VALUES (?, ?)""", (resource_tuple_list))

    database_connection.commit()
    
    return 

def set_resources_commodities_table(resource_tuple_list):
    
    database_connection = db.get_db()
    
    database_connection.executemany("""INSERT INTO 'city_resources_commodities ' (id, name) VALUES (?, ?)""", (resource_tuple_list))

    database_connection.commit()
    
    return 