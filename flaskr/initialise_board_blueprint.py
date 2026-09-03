from flask import (
    Blueprint, g, redirect, render_template, request, url_for
)

from .helper_classes.settlement import Settlement
from .helper_classes.settler import Settler

from .helper_modules import (calculate_row_id,
                            get_settlers, 
                            get_settlements,
                            get_resources,
                            insert_settlement_into_settlements_table,
                            row_objects_to_classes,
                            update_game_progress)

bp = Blueprint('initialise_board', __name__, url_prefix='/initialise_board/')

@bp.route('/place_settlement', methods =['GET', 'POST'])
def place_settlement():
    
    update_game_progress.update_game_progress("initial settlement placement")

    settlers = row_objects_to_classes.row_objects_to_classes(Settler, get_settlers.get_settlers())

    settlement_settler_ids = [settlement.settler_id for settlement in row_objects_to_classes.row_objects_to_classes(Settlement, get_settlements.get_settlements())]

    settlers_with_no_victory_points = [settler for settler in settlers if settler.id not in settlement_settler_ids]   

    if request.method == 'POST':

        current_settler = settlers_with_no_victory_points.pop(0)
        settlement_id = calculate_row_id.calculate_row_id("settlements")
        insert_settlement_into_settlements_table.insert_settlement_into_settlements_table({'settlement_id': settlement_id,
                'settler_id': current_settler['id'],
                'resource_1': request.form['resource_1'], 'roll_1': request.form['roll_1'],
                'resource_2': request.form['resource_2'], 'roll_2': request.form['roll_2'],
                'resource_3': request.form['resource_3'], 'roll_3': request.form['roll_3'],
                'is_city': False})
           
    resources = get_resources.get_resources()  
    
    if settlers_with_no_victory_points:
        return render_template('place_settlement.html', settler_to_place_settlement_name = settlers_with_no_victory_points[0].username,
                        have_all_settlers_placed_a_settlement = False,
                        resources = resources)      
    else:
        return render_template('place_settlement.html', 
                        have_all_settlers_placed_a_settlement = True,
                        resources = resources)

@bp.route('/place_city', methods =['GET', 'POST'])
def place_city():

    update_game_progress.update_game_progress("initial settlement placement")

    settlers = get_settlers.get_settlers()

    settlers_with_one_victory_points = [settler for settler in settlers if settler['victory_points'] == 1]   

    if request.method == 'POST':

        current_settler = settlers_with_one_victory_points.pop()
        settlement_id = calculate_row_id.calculate_row_id("settlements")
        insert_settlement_into_settlements_table.insert_settlement_into_settlements_table({'settlement_id': settlement_id,
                'settler_id': current_settler['id'],
                'resource_1': request.form['resource_1'], 'roll_1': request.form['roll_1'],
                'resource_2': request.form['resource_2'], 'roll_2': request.form['roll_2'],
                'resource_3': request.form['resource_3'], 'roll_3': request.form['roll_3'],
                'is_city': True})
            
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
