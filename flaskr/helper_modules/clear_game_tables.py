from .. import db

def clear_game_tables():
  	
    database_connection = db.get_db()
    
    for game_data_table in ['game_progress' 'settlers', 'settlements', 'knights', 'settlers_that_contributed_least_to_catans_defence','resources', 'city_resources_commodities']:
        database_connection.execute(f"""DELETE FROM {game_data_table}""")

    database_connection.commit()

    return