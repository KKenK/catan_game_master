from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from .helper_modules import get_settlers, populate_resources_commodities_table, insert_settler_into_settlers_table, calculate_row_id

bp = Blueprint('initialise_settlers',__name__, url_prefix='/initialise_settlers/')

@bp.route('/')
def select_number_of_players():
    return render_template('select_number_of_players.html')


@bp.route('/register_settler', methods=['GET','POST'])
def register_settlers():
    next_settler_id = calculate_row_id.calculate_row_id('settlers')

    if request.method == 'POST':
        settler_name = request.form['name']

        insert_settler_into_settlers_table.insert_settler_into_settlers_table(settler_name)

    minimum_players_required = False
    maximum_players_reached = False

    if next_settler_id >= 1:
        minimum_players_required = True
    if next_settler_id >= 5:
        maximum_players_reached = True

    return render_template('register_settler.html', next_settler_number = next_settler_id + 1, maximum_settler_reached = maximum_players_reached, minimum_players_required = minimum_players_required)