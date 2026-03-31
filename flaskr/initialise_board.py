# place_settlement.py
from flask import (
    Blueprint, g, redirect, render_template, request, url_for
)

from . import db
from .helper_modules import get_settlers, get_resources
bp = Blueprint('initialise_board', __name__, url_prefix='/initialise_board/')

@bp.route('/place_settlement')
def place_settlement():
    settlers = get_settlers.get_settlers(db.database_connector)
    resources = get_resources.get_resources(db.database_connector)
    current_settler = [settler for settler in settlers if settlers.victory_points == 0][0]
    is_last_player = current_settler.id == len(settlers)
    return render_template('initalise_board/place_settlement.html', current_settler_name = current_settler['name'], is_last_player = is_last_player, resources = resources)

@bp.route('/place_city')
def place_city():
    settlers = get_settlers.get_settlers(db.database_connector)
    resources = get_resources(db.database_connector)
    current_settler = [settler for settler in settlers if settlers.victory_points == 1][0]
    is_last_player = current_settler.id == len(players)
    return render_template('initalise_board/place_city.html', current_settler = current_settler, is_last_player = is_last_player, resources = resources)
# get_first_player_without_settlement.py
def get_first_player_without_settlement(database_connector):
    with databse_connector() as db:
    	return db.execute("""SELECT * FROM settlers WHERE victory_points = 0 LIMIT 1""").fetchone()

def get_last_player_without_city(database_connector):
    with databse_connector() as db:
    	return db.execute("""SELECT * FROM settlers WHERE victory_points = 1 ORDER BY id DESC LIMIT 1""").fetchone()

def get_players(database_connector):
    with databse_connector() as db:
    	return db.execute("""SELECT * FROM settlers""").fetchall()

def get_resources(database_connector):
    with databse_connector() as db:
    	return db.execute("""SELECT * FROM resources""").fetchall()
      
#