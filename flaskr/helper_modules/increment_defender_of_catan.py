from .. import db

def increment_defender_of_catan(settler_id, increment_value = 1):

    database_connection = db.get_db()

    database_connection.execute("""UPDATE settlers SET defender_of_catan = defender_of_catan + (?) WHERE id = (?)""", (increment_value, settler_id,))

    database_connection.commit()

    return