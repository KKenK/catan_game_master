import sqlite3

import click
from flask import current_app, g

class DatabaseConnector():

    def __enter__(self): 
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row

        return g.db

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            if 'db' in g:
                g.db.close()
            
            print('exited normally')
            
        else:
            print('raise an exception! ' + str(exc_type))
            
            return False
        
class DatabaseInitialisor():
    def __init__(self, DatabaseConnector):
        self.DatabaseConnector = DatabaseConnector
    
    def init_db(self):
        with self.DatabaseConnector() as db:

            with current_app.open_resource('schema.sql') as f:
                db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    try:
        databaseInitialisor = DatabaseInitialisor(DatabaseConnector)
        databaseInitialisor.init_db()
        click.echo('Initialized the database.')
    except sqlite3.OperationalError as operational_error:
        raise ValueError('Database tables already exist. Manually remove them?', operational_error)
def init_app(app):
    app.cli.add_command(init_db_command)
