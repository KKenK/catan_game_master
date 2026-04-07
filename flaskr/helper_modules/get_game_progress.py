def get_game_progress(database_connector):
    with database_connector() as db:
    	return db.execute("""SELECT 'progress' FROM game_progress""").fetchone()
  