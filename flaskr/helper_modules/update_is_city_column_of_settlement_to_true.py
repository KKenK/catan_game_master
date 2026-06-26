from .. import db

def update_is_city_column_of_settlement_to_true(settlement_id):
    
    database_connection = db.get_db()
    
    database_connection.execute("""UPDATE 'settlements' SET (is_city) = (1) WHERE id = (?) """, (settlement_id,))

    database_connection.commit()
    