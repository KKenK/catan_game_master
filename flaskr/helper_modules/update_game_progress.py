def update_game_progress(database_connector, game_status):
    with database_connector() as db:
        db.execute("""UPDATE INTO 'game_progress' (progress) VALUES (?)""", (game_status,))