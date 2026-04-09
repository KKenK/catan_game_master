def clear_game_tables(database_connector):
    with database_connector() as db:
        db.execute("""DELETE FROM 'settlers';
        DELETE FROM 'settlements';
        DELETE FROM 'knights';
        DELETE FROM 'resources';
        DELETE FROM 'city_resources_comodities';""")
