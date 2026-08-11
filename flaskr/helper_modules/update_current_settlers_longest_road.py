from .. import db

def update_current_settlers_longest_road(updated_longest_road, settler_id):
    
    database_connection = db.get_db()
    
    database_connection.execute("""UPDATE 'settlers' SET longest_road = ? WHERE id = ?""", (updated_longest_road, settler_id))

    database_connection.commit()