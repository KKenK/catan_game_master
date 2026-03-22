def populate_resources_table(database_connector):
    
    with database_connector() as db:
        db.execute("""INSERT INTO 'resources_comodoties' VALUES
                               ('Wood'),  
                               ('Brick'),
                               ('Sheep'),
                               ('Wheat'),
                               ('Ore');""")
    
def populate_city_resources_comodities_table(database_connector):
    
    with database_connector() as db:
        db.execute("""INSERT INTO 'resources_comodoties' VALUES
                               ('Paper'),  
                               ('Brick'),
                               ('Cloth'),
                               ('Wheat'),
                               ('Coin');""")