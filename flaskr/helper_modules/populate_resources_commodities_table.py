from .. import db

def populate_resources_table():
    
    database_connection = db.get_db()
    
    database_connection.execute("""INSERT INTO 'resources' VALUES
                               ('Wood'),  
                               ('Brick'),
                               ('Sheep'),
                               ('Wheat'),
                               ('Ore');""")
    
def populate_city_resources_comodities_table():
    
    database_connection = db.get_db()
    
    database_connection.execute("""INSERT INTO 'city_resources_comodoties' VALUES
                               ('Paper'),  
                               ('Brick'),
                               ('Cloth'),
                               ('Wheat'),
                               ('Coin');""")