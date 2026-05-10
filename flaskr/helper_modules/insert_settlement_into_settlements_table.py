from .. import db
from . import calculate_row_id 

def insert_settlement_into_settlements_table(settlement):

    settlement_id = calculate_row_id.calculate_row_id("settlements")

    database_connection = db.get_db()

    database_connection.execute("""INSERT INTO 'settlements' (id, settler_id, 
                                resource_1, roll_1,
                                resource_2, roll_2,
                                resource_3, roll_3,
                                is_city)
                                VALUES (?,?,?,?,?,?,?,?,?)""", (settlement_id, settlement['settler_id'],
                                settlement['resource_1'], settlement['roll_1'],
                                settlement['resource_2'], settlement['roll_2'],
                                settlement['resource_3'], settlement['roll_3'],
                                settlement['is_city']))

    database_connection.commit()

    return