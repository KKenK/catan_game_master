from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from .helper_modules import (get_game_progress, 
                             get_settler_turn, 
                             get_settlers, 
                             get_knights, 
                             get_resources_and_commodities, 
                             get_settlements, 
                             calculate_row_id, 
                             update_game_progress,
                             update_settler_turn,
                             insert_knight_into_knight_table,
                             activate_knight,
                             deactivate_knight,
                             insert_settlement_into_settlements_table,
                             increment_victory_points,
                             get_resources)

bp = Blueprint('game_in_progress',__name__, url_prefix='/game')

@bp.route('/')
def game():
    
    if get_game_progress.get_game_progress() != "game_in_progress":
            update_game_progress.update_game_progress("game_in_progress")

    settlers = get_settlers.get_settlers()
    settler_ids = sorted([settler['id'] for settler in settlers])
    knights = get_knights.get_knights()

    knights_settler_ids = list(set([knight['settler_id'] for knight in knights]))
    #print(f"knights_settler_ids: {knights_settler_ids}")

    list_of_active_knights_by_settler_id = [[knight['level'] for knight in knights if knight['settler_id'] == knight_settler_id and knight['is_active']] for knight_settler_id in knights_settler_ids]
    #print(f"list_of_active_knights_by_settler_id: {list_of_active_knights_by_settler_id}")
    
    id_of_next_knight_to_be_built = len(knights)

    knight_strength_dict = {knights_settler_ids[i] : sum(list_of_active_knights_by_settler_id[i]) for i in range(len(knights_settler_ids))}
    #print(f"knight_strength_dict: {knight_strength_dict}")
    
    settler_table_keys = list(settlers[0].keys())
    settlers_dict = {settler['id'] : {settler_table_key : settler[settler_table_key] for settler_table_key in settler_table_keys} for settler in settlers}
    #print (f"settler_dict: {settlers_dict}")

    for settler in settlers:

        settlers_dict[settler['id']]['army_strength'] = 0 if settler['id'] not in knights_settler_ids else knight_strength_dict[settler['id']]
        settlers_dict[settler['id']]['knights'] = [knight for knight in knights if knight['settler_id'] == settler['id']]

    settlements = get_settlements.get_settlements()

    route_is_game_index = True if not request.path.split('/')[-1].isdigit() else False
    link_prefix = '' if route_is_game_index else '../'

    return render_template('game_page.html', settler_ids = settler_ids, settler_dicts = settlers_dict, id_of_next_knight_to_be_built = id_of_next_knight_to_be_built, link_prefix = link_prefix)

@bp.route('/start_turn')
def start_turn():

    game_progress = get_settler_turn.get()

    settler_turn = game_progress['settler_turn']

    is_settler_two = game_progress['is_settler_two']

    settlers = get_settlers.get_settlers()

    if get_game_progress.get_game_progress() == 'start_turn':
        
        return render_template('start_turn.html', settler_turn = settler_turn, settler_username = settlers[settler_turn]['username'], is_settler_two = is_settler_two)
    
    update_game_progress.update_game_progress('start_turn')
    
    number_of_settlers = len(settlers)

    if number_of_settlers > 4:
        is_settler_two = 1 if not is_settler_two else 0

    settler_turn += 3 if is_settler_two else 1

    if settler_turn >= number_of_settlers:
        settler_turn -= number_of_settlers

    update_settler_turn.update_settler_turn(settler_turn, is_settler_two)

    return render_template('start_turn.html', settler_turn = settler_turn, settler_username = settlers[settler_turn]['username'], is_settler_two = is_settler_two)

@bp.route('/collect_resources', methods=['POST'])
def collect_resources():
    
    number_rolled = int(request.form['dice_roll'])
    
    settlers = get_settlers.get_settlers()
    
    settlements = get_settlements.get_settlements()

    settlements_dict = {settlement['id']: {'settler_id': settlement['settler_id'],
                                           'rolls': [(settlement['roll_1'], settlement['resource_1']),
                                           (settlement['roll_2'], settlement['resource_2']),
                                           (settlement['roll_3'], settlement['resource_3'])],
                                           'is_city': settlement['is_city']}
                                           for settlement in settlements}

    resources_and_commodities = get_resources_and_commodities.get_resources_and_commodities()
    resources_and_commodities_dict = {item['id']: {'settlement': item[1], 'city': item[2]} for item in resources_and_commodities}

    settlers_to_collect_dict = {settler['id'] : [] for settler in settlers}
  
    for settler in settlers:
        
        items_to_collect_list = []
        
        for settlement in settlements_dict.values(): 
            
            if settler['id'] != settlement['settler_id']:
                continue
                
            for roll in settlement['rolls']:
                if roll[0] != number_rolled:
                      continue

                items_to_collect_list.append(resources_and_commodities_dict[roll[1]]['settlement'])
                
                if settlement['is_city']:
                    items_to_collect_list.append(resources_and_commodities_dict[roll[1]]['city'])    
        
        settlers_to_collect_dict[settler['id']] = {item : items_to_collect_list.count(item) for item in set(items_to_collect_list)}
    
    print(settlers_to_collect_dict)     

    return render_template('collect_resources.html', settlers = settlers, settlers_to_collect_dict = settlers_to_collect_dict)

@bp.route('/build_settlement')
def build_settlement():
    
    settlers = get_settlers.get_settlers()

    settler_turn_id = get_settler_turn.get()['settler_turn']

    settlement_id = calculate_row_id.calculate_row_id("settlements")
    insert_settlement_into_settlements_table.insert_settlement_into_settlements_table({'settlement_id': settlement_id,
            'settler_id': settler_turn_id,
            'resource_1': request.form['resource_1'], 'roll_1': request.form['roll_1'],
            'resource_2': request.form['resource_2'], 'roll_2': request.form['roll_2'],
            'resource_3': request.form['resource_3'], 'roll_3': request.form['roll_3'],
            'is_city': False})
        
    increment_victory_points.increment_victory_points(settler_turn_id)
    
    resources = get_resources.get_resources()  
    

    return render_template('place_settlement.html', settler_to_place_settlement_name = settlers[settler_turn_id]['username'],

                        resources = resources)      

@bp.route('/build_knight/<int:knight_id>')
def build_knight(knight_id):
        
    settler_turn_id = get_settler_turn.get()['settler_turn']

    insert_knight_into_knight_table.insert_knight(settler_turn_id, knight_id)

    return game()

@bp.route('/activate_knight/<int:knight_id>')
def knight_activation(knight_id):
  	
    activate_knight.activate_knight(knight_id)
  
    return game()

@bp.route('/deactivate_knight/<int:knight_id>')
def knight_deactivation(knight_id):
  	
    deactivate_knight.deactivate_knight(knight_id)
  
    return game()
