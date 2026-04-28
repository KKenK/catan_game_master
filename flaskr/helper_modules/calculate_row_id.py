from .. import db

def calculate_row_id(table):
	    
    return db.get_db().execute(f"""SELECT COUNT() FROM {table} """).fetchone()[0]
    