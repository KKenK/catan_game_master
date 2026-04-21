# Returns a list of resources from the resources table
from .. import db

def get_resources(database_connector):
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM resources""").fetchall()