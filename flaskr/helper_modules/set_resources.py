from .. import db
from . import resources

def set_resources(resource_tuple_list):
    
    database_connection = db.get_db()
    
    database_connection.executemany("""INSERT INTO 'resources' (id, resource) VALUES (?, ?)""", (resources[resource_tuple_list]))

    database_connection.commit()
    
    return 
  