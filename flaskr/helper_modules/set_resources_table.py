from .. import db
from . import resources

def set_resources_commodoties(resource_tuple_list):
    
    database_connection = db.get_db()
    
    database_connection.executemany("""INSERT INTO 'resources' (id, resource) VALUES (?, ?)""", (resource_tuple_list))

    database_connection.commit()
    
    return 
  