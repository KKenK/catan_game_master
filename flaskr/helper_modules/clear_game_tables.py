def clear_game_tables(database_connector):
    with database_connector() as db:
      	for game_data_table in [ 'settlers', 'settlements', 'knights', 'resources', 'city_resources_commodities' ]:
    	    db.execute(f"""DELETE FROM {game_data_table}""")
