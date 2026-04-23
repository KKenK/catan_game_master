from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from .helper_modules import get_settlers, populate_resources_commodities_table, insert_settler_into_settlers_table

bp = Blueprint('initialise_settlers',__name__, url_prefix='/initialise_settlers/')

@bp.route('/')
def select_number_of_players():
    return render_template('select_number_of_players.html')


@bp.route('/register_settler', methods=['GET','POST'])
def register_settlers():
    if request.method == 'GET':
        settlers = get_settlers.get_settlers()

        if settlers:
            player_id = settlers[-1]['id']
        else:
            player_id = 0
    
    elif request.method == 'POST':
        player_name = request.form['name']

        player_id = insert_settler_into_settlers_table.insert_settler_into_settlers_table(player_name)

    minimum_players_required = False
    maximum_players_reached = False
    
    if player_id >= 2:
        minimum_players_required = True
    if player_id >= 6:
        maximum_players_reached = True
    
    return render_template('register_settler.html', player_number = player_id + 1, maximum_players_reached = maximum_players_reached, minimum_players_required = minimum_players_required)