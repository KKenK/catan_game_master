from .. import db

def get_settlements():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT * FROM settlements""").fetchall()

def get_settlements_with_resource_name():
    
    database_connection = db.get_db()
    
    return database_connection.execute("""SELECT settlements.id,
    settler_id,
    resources_1.name AS resource_1_text,
    roll_1,
    resources_2.name AS resource_2_text,
    roll_2,
    resources_3.name AS resource_3_text,
    roll_3,
    is_city FROM settlements
    LEFT JOIN resources AS resources_1 ON settlements.resource_1 = resources_1.id
    LEFT JOIN resources AS resources_2 ON settlements.resource_2 = resources_2.id
    LEFT JOIN resources AS resources_3 ON settlements.resource_3 = resources_3.id""").fetchall()