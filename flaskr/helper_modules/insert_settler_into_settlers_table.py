def insert_settler_into_settlers_table(database_connector, username):
  
    with database_connector() as db:
        return db.execute("""INSERT INTO 'settlers' (username) VALUES (?) RETURNING id""", (username,)).fetchone()[0]