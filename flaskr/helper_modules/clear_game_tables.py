from .. import db

def clear_game_tables():
  	
    database_connection = db.get_db()
    
    for game_data_table in [ 'settlers', 'settlements', 'knights', 'resources', 'city_resources_commodities' ]:
        database_connection.execute(f"""DELETE FROM {game_data_table}""")