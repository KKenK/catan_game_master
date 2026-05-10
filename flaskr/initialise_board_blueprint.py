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
    
    resources = get_resources.get_resources()  
    
    if settlers_with_no_victory_points:
        return render_template('initialise_board/place_settlement.html', settler_to_place_settlement_name = settlers_with_no_victory_points[0]['username'],
                        have_all_settlers_placed_a_settlement = False,
                        resources = resources)      
    else:
        return render_template('initialise_board/place_settlement.html', 
                        have_all_settlers_placed_a_settlement = True,
                        resources = resources)

@bp.route('/place_city', methods =['GET', 'POST'])
def place_city():

    update_game_progress.update_game_progress("initial settlement placement")

    settlers = get_settlers.get_settlers()

    settlers_with_one_victory_points = [settler for settler in settlers if settler['victory_points'] == 1]   

    if request.method == 'POST':

        current_settler = settlers_with_one_victory_points.pop()

        insert_settlement_into_settlements_table.insert_settlement_into_settlements_table({'settler_id': current_settler['id'],
                'resource_1': request.form['resource_1'], 'roll_1': request.form['roll_1'],
                'resource_2': request.form['resource_2'], 'roll_2': request.form['roll_2'],
                'resource_3': request.form['resource_3'], 'roll_3': request.form['roll_3'],
                'is_city': True})
        
        increment_victory_points.increment_victory_points(current_settler['id'], increment_value = 2)
    
    if not settlers_with_one_victory_points:
        have_all_settlers_placed_a_city = True
        current_settler = {'username' : 'All settlements places!',}
    else:
        current_settler = settlers_with_one_victory_points[-1]
        have_all_settlers_placed_a_city = False
    
    resources = get_resources.get_resources()
    
    return render_template('initialise_board/place_city.html', settler_to_place_city_name = current_settler['username'],
                            have_all_settlers_placed_a_city = have_all_settlers_placed_a_city,
                            resources = resources)
