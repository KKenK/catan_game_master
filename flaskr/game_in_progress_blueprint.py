from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from .helper_modules import get_game_progress, get_settler_turn, get_settlers, get_knights, get_settlements, update_game_progress, update_settler_turn

bp = Blueprint('game_in_progress',__name__, url_prefix='/game')

@bp.route('/')
def game():
    
    if get_game_progress.get_game_progress() != "game_in_progress":
            update_game_progress.update_game_progress("game_in_progress")

    settlers = get_settlers.get_settlers()
    settler_ids = sorted([settler['id'] for settler in settlers])
    knights = get_knights.get_knights()
    print(f"knights: {knights}")

    knights_settler_ids = list(set([knight['settler_id'] for knight in knights]))
    print(f"knights_settler_ids: {knights_settler_ids}")

    list_of_active_knights_by_settler_id = [[knight['level'] for knight in knights if knight['settler_id'] == knight_settler_id and knight['is_active']] for knight_settler_id in knights_settler_ids]
    print(f"list_of_active_knights_by_settler_id: {list_of_active_knights_by_settler_id}")
    
    knight_strength_dict = {knights_settler_ids[i] : sum(list_of_active_knights_by_settler_id[i]) for i in range(len(knights_settler_ids))}
    print(f"knight_strength_dict: {knight_strength_dict}")
    
    settler_table_keys = list(settlers[0].keys())
    settlers_dict = {settler['id'] : {settler_table_key : settler[settler_table_key] for settler_table_key in settler_table_keys} for settler in settlers}
    print (f"settler_dict: {settlers_dict}")

    for settler in settlers:

        settlers_dict[settler['id']]['army_strength'] = 0 if settler['id'] not in knights_settler_ids else knight_strength_dict[settler['id']]
        settlers_dict[settler['id']]['knights'] = "None"

    settlements = get_settlements.get_settlements()

    return render_template('game_page.html', settler_ids = settler_ids, settler_dicts = settlers_dict)

@bp.route('/roll_dice')
def roll_dice():
    number_of_settlers = len(get_settlers.get_settlers())

    return render_template('roll_dice.html')

