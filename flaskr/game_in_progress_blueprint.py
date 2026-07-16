from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from .helper_modules import (get_game_progress,
                             get_game_progress_data,
                             get_settler_turn, 
                             get_settlers, 
                             get_settlers_that_contributed_least_to_catans_defence,
                             get_knights, 
                             get_resources_and_commodities, 
                             get_settlements,
                             get_cities,
                             get_settlements_with_resource_name,
                             calculate_row_id, 
                             update_game_progress,
                             update_settler_turn,
                             insert_knight_into_knight_table,
                             activate_knight,
                             deactivate_knight,
                             insert_settlement_into_settlements_table,
                             increment_victory_points,
                             increment_knights_level,
                             decrement_the_barbarians_distance_from_catan,
                             get_resources,
                             reset_barbarians_distance_from_catan,
                             insert_settler_into_settlers_that_contributed_least_to_catans_defence_table,
                             remove_first_settler_from_settlers_that_contributed_least_to_catans_defence_table,
                             update_is_city_column_of_settlement_to_true,
                             update_is_city_column_of_settlement_to_false)

bp = Blueprint('game_in_progress',__name__, url_prefix='/game')

@bp.route('/')
def game():
    
    game_progress = get_game_progress_data.get_game_progress_data()

    if game_progress['progress'] != "game_in_progress":
            update_game_progress.update_game_progress("game_in_progress")

    settlers = get_settlers.get_settlers()
    
    settler_turn_id = game_progress['settler_turn']
    settlers_turn_username =  settlers[settler_turn_id]['username']

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

    active_knights_count = sum(knight_strength_dict.values())

    barbarian_strength = len([settlement for settlement in settlements if settlement['is_city']])

    route_is_game_index = True if not request.path.split('/')[-1].isdigit() else False
    link_prefix = '' if route_is_game_index else '../'

    return render_template('game_page.html', settler_ids = settler_ids, settlers_turn_username = settlers_turn_username, active_knights_count = active_knights_count, barbarian_strength = barbarian_strength, barbarians_distance_from_catan = game_progress['barbarians_distance_from_catan'], settler_dicts = settlers_dict, id_of_next_knight_to_be_built = id_of_next_knight_to_be_built, link_prefix = link_prefix)

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
    
    event_rolled = request.form['event_dice_roll']
    
    if event_rolled == 'barbarian_ship':
        
        decrement_the_barbarians_distance_from_catan.decrement_the_barbarians_distance_from_catan()

    barbarians_distance_from_catan = get_game_progress_data.get_game_progress_data()['barbarians_distance_from_catan']

    barbarians_attack = True if not barbarians_distance_from_catan else False

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

    return render_template('collect_resources.html', settlers = settlers, settlers_to_collect_dict = settlers_to_collect_dict, barbarians_attack = barbarians_attack)

@bp.route('/barbarians_attack')
def barbarians_attack():

    reset_barbarians_distance_from_catan.reset_barbarians_distance_from_catan()
    
    settlers = get_settlers.get_settlers()

    knights = get_knights.get_knights()

    settlements = get_settlements.get_settlements()

    settler_army_dict = {settler['id'] : sum([knight['level'] for knight in knights if knight['settler_id'] == settler['id'] and knight['is_active']])
                         for settler in settlers}
    
    list_of_active_army_strengths = [settler_army_strength for settler_army_strength in settler_army_dict.values()]

    army_strength_of_catan = sum(list_of_active_army_strengths)

    settlements =  get_settlements.get_settlements()

    barbarian_strength = len([settlement for settlement in settlements if settlement['is_city']])

    victory_for_catan = True if army_strength_of_catan >= barbarian_strength else False

    cities = [settlement for settlement in settlements if settlement['is_city']]

    settler_ids_of_settlers_with_cities = set([city['settler_id'] for city in cities])

    settler_ids_with_weakest_army_and_cities = []
        
    if not victory_for_catan:

        sorted(list_of_active_army_strengths)
        
        while not settler_ids_with_weakest_army_and_cities:

            weakest_army = list_of_active_army_strengths.pop(0)

            settlers_with_weakest_army = [settlers[settler_id] for settler_id in settler_army_dict if settler_army_dict[settler_id] == weakest_army]

            settler_ids_with_weakest_army_and_cities = [settler['id'] for settler in settlers_with_weakest_army if settler['id'] in settler_ids_of_settlers_with_cities]

            if weakest_army:
                continue
            break

        if settler_ids_with_weakest_army_and_cities:
            insert_settler_into_settlers_that_contributed_least_to_catans_defence_table.insert_settler_into_settlers_that_contributed_least_to_catans_defence_table(settler_ids_with_weakest_army_and_cities)

        return render_template('barbarians_attack.html', victory_for_catan = victory_for_catan)

    else:    
        largest_army = max(list_of_active_army_strengths)

        settlers_with_largest_army = [settlers[settler_id] for settler_id in settler_army_dict if settler_army_dict[settler_id] == largest_army]

        is_tie = True if len(settlers_with_largest_army) > 1 else False

        return render_template('barbarians_attack.html', victory_for_catan = victory_for_catan, is_tie = is_tie, settlers_with_largest_army = settlers_with_largest_army)

@bp.route('/select_city_to_demote', methods = ['GET','POST'])
def select_city_to_demote():
    
    update_game_progress.update_game_progress('resolving_defeat')

    settlers_who_contributed_least_to_catans_defence = get_settlers_that_contributed_least_to_catans_defence.get_settlers_that_contributed_least_to_catans_defence()
    
    if request.method == 'POST' and settlers_who_contributed_least_to_catans_defence:
        update_is_city_column_of_settlement_to_false.update_is_city_column_of_settlement_to_false(request.form.get('city_id'))
        remove_first_settler_from_settlers_that_contributed_least_to_catans_defence_table.remove_settler_from_settlers_that_contributed_least_to_catans_defence_table(settlers_who_contributed_least_to_catans_defence[0]['id'])
    
    if not settlers_who_contributed_least_to_catans_defence:
        return render_template('select_city_to_demote.html', defeat_resolved = True)
    
    settlers = get_settlers.get_settlers()

    cities = get_cities.get_cities()

    settler_to_demote_city_id = settlers_who_contributed_least_to_catans_defence[0]['id']

    cities_of_settler_to_demote = [city for city in cities if city['settler_id'] == settler_to_demote_city_id]

    return render_template('select_city_to_demote.html', defeat_resolved = False, settler_username = settlers[settler_to_demote_city_id]['username'], cities_of_settler_to_demote = cities_of_settler_to_demote)

@bp.route('/build_settlement')
def build_settlement():
    
    settler_turn_id = get_settler_turn.get()['settler_turn']  
    
    settlers = get_settlers.get_settlers()
    
    resources = get_resources.get_resources()  

    return render_template('place_settlement.html', settler_to_place_settlement_name = settlers[settler_turn_id]['username'],
                        have_all_settlers_placed_a_settlement = False,
                        resources = resources)    

@bp.route('/place_settlement', methods=['POST'])
def place_settlement():

    settler_turn_id = get_settler_turn.get()['settler_turn']

    settlement_id = calculate_row_id.calculate_row_id("settlements")
    insert_settlement_into_settlements_table.insert_settlement_into_settlements_table({'settlement_id': settlement_id,
            'settler_id': settler_turn_id,
            'resource_1': request.form['resource_1'], 'roll_1': request.form['roll_1'],
            'resource_2': request.form['resource_2'], 'roll_2': request.form['roll_2'],
            'resource_3': request.form['resource_3'], 'roll_3': request.form['roll_3'],
            'is_city': False})
        
    increment_victory_points.increment_victory_points(settler_turn_id)

    return game()

@bp.route('/build_knight/<int:knight_id>')
def build_knight(knight_id):
        
    settler_turn_id = get_settler_turn.get()['settler_turn']

    insert_knight_into_knight_table.insert_knight(settler_turn_id, knight_id)

    return game()

@bp.route('/select_knights_to_promote')
def select_knights_to_promote():
    knights = get_knights.get_knights()

    current_settlers_turn_knights = [knight for knight in knights if knight['settler_id'] == get_settler_turn.get()['settler_turn']]
    
    return render_template('select_knights_to_promote.html', current_settlers_turn_knights = current_settlers_turn_knights)

@bp.route('/promote_knight', methods=['POST'])
def promote_knight():
    
    knight_ids = [knight_id for knight_id in request.form.values()]
    
    increment_knights_level.increment_knights_level(tuple(knight_ids))

    return game()

@bp.route('/activate_knight/<int:knight_id>')
def knight_activation(knight_id):
  	
    activate_knight.activate_knight(knight_id)
  
    return game()

@bp.route('/deactivate_knight/<int:knight_id>')
def knight_deactivation(knight_id):
  	
    deactivate_knight.deactivate_knight(knight_id)
  
    return game()

@bp.route('select_settlement_to_promote')
def select_settlement_to_promote():

    settler_turn_id = get_settler_turn.get()['settler_turn']

    settlements_with_resource_name = get_settlements_with_resource_name.get_settlements_with_resource_name()

    settler_whose_turn_it_is_settlements = [settlement for settlement in settlements_with_resource_name if settlement['settler_id'] == settler_turn_id]

    return render_template('select_settlement_to_promote.html', settler_whose_turn_it_is_settlements = settler_whose_turn_it_is_settlements)

@bp.route('/promote_settlement/<int:settlement_id>')
def promote_settlement(settlement_id):
    
    update_is_city_column_of_settlement_to_true.update_is_city_column_of_settlement_to_true(settlement_id)

    increment_victory_points.increment_victory_points(get_settler_turn.get()['settler_turn'])

    return game()
