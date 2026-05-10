from flask import (
    Blueprint, g, redirect, render_template, request, url_for
)

from .helper_modules import (get_settlers, 
                            get_resources,
                            update_game_progress, 
                            insert_settlement_into_settlements_table,
                            increment_victory_points)

bp = Blueprint('initialise_board', __name__, url_prefix='/initialise_board/')

@bp.route('/place_settlement', methods =['GET', 'POST'])
def place_settlement():
    
    update_game_progress.update_game_progress("initial settlement placement")

    settlers = get_settlers.get_settlers()

    settlers_with_no_victory_points = [settler for settler in settlers if settler['victory_points'] == 0]   

    if request.method == 'POST':

        current_settler = settlers_with_no_victory_points.pop(0)

        insert_settlement_into_settlements_table.insert_settlement_into_settlements_table({'settler_id': current_settler['id'],
                'resource_1': request.form['resource_1'], 'roll_1': request.form['roll_1'],
                'resource_2': request.form['resource_2'], 'roll_2': request.form['roll_2'],
                'resource_3': request.form['resource_3'], 'roll_3': request.form['roll_3'],
                'is_city': False})
        
        increment_victory_points.increment_victory_points(current_settler['id'])
    
    if not settlers_with_no_victory_points:
        have_all_settlers_placed_a_settlement = True
        current_settler = {'username' : 'All settlements places!',}
    else:
        current_settler = settlers_with_no_victory_points[0]
        have_all_settlers_placed_a_settlement = False
    
    resources = get_resources.get_resources()
    
    return render_template('initialise_board/place_settlement.html', current_settler_name = current_settler['username'],
                            have_all_settlers_placed_a_settlement = have_all_settlers_placed_a_settlement,
                            resources = resources)

@bp.route('/place_city')
def place_city():
    update_game_progress.update_game_progress("initial city placement")
    settlers = get_settlers.get_settlers()
    resources = get_resources.get_resources()
    current_settler = [settler for settler in settlers if settler['victory_points'] == 1][-1]
    have_all_settlers_placed_a_city = True if current_settler['id'] == len(settlers) else False
    return render_template('initialise_board/place_city.html', current_settler_name = current_settler['username'],
                            have_all_settlers_placed_a_city = have_all_settlers_placed_a_city,
                            resources = resources)