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
 
    if request.method == 'POST':
        settler_name = request.form['name']

        insert_settler_into_settlers_table.insert_settler_into_settlers_table(settler_name)
    
    next_settler_id = calculate_row_id.calculate_row_id('settlers')
    
    minimum_settlers_required = False
    maximum_settlers_reached = False

    if next_settler_id >= 2:
        minimum_settlers_required = True
    if next_settler_id >= 6:
        maximum_settlers_reached = True


    return render_template('register_settler.html', next_settler_number = next_settler_id + 1, maximum_settlers_reached = maximum_settlers_reached, minimum_settlers_required = minimum_settlers_required)