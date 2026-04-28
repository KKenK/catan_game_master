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
            settler_id = settlers[-1]['id']
        else:
            settler_id = 0
    
    elif request.method == 'POST':
        settler_name = request.form['name']

        settler_id = insert_settler_into_settlers_table.insert_settler_into_settlers_table(settler_name)

    minimum_players_required = False
    maximum_players_reached = False
    
    if settler_id >= 2:
        minimum_players_required = True
    if settler_id >= 6:
        maximum_players_reached = True
    
    return render_template('register_settler.html', settler_number = settler_id + 1, maximum_settler_reached = maximum_players_reached, minimum_players_required = minimum_players_required)