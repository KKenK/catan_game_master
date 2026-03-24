# Returns a list of resources from the resources table

def get_resources(database_connector):
    with database_connector() as db:
        return db.execute("""SELECT * FROM resources""").fetchall()