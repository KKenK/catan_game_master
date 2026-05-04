from .. import db

def set_resources_table(resource_tuple_list):
    
    database_connection = db.get_db()
    
    database_connection.executemany("""INSERT INTO 'resources' (id, resource) VALUES (?, ?)""", (resource_tuple_list))

    database_connection.commit()
    
    return 
  