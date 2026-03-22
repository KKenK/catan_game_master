from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from . import db
from .helper_modules import populate_resources_comodoties_table, insert_player_into_settlers_table

bp = Blueprint('initialise_players',__name__, url_prefix='/initialise_players/')

@bp.route('/')
def select_number_of_players():
    return render_template('select_number_of_players.html')

@bp.route('/register_player', methods=['GET'])
def register_first_player():
    
    return render_template('initialise_players/register_player.html', player_number = 1, maximum_players_reached = False, minimum_players_required = False)

@bp.route('/register_player', methods=['POST'])
def register_players():

    player_name = request.form['name']
    
    player_id = insert_player_into_settlers_table.insert_player_into_settlers_table(db.DatabaseConnector, player_name)
    
    minimum_players_required = False
    maximum_players_reached = False
    
    if player_id >= 2:
        minimum_players_required = True
    if player_id >= 6:
        maximum_players_reached = True
    
    return render_template('initialise_players/register_player.html', player_number = player_id + 1, maximum_players_reached = maximum_players_reached, minimum_players_required = minimum_players_required)
    
