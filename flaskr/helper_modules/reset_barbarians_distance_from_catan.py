from .. import db

def reset_the_barbarians_distance_from_catan():

    database_connection = db.get_db()

    database_connection.execute("""UPDATE game_progress SET barbarians_distance_from_catan = 7""")

    database_connection.commit()

    return