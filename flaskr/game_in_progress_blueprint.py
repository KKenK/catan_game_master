from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from .helper_modules import get_game_progress, get_settlers, get_knights, get_settlements, update_game_progress, update_settler_turn

bp = Blueprint('game_in_progress',__name__, url_prefix='/game')

@bp.route('/')
def game():
    
    if get_game_progress.get_game_progress() != "game_in_progress":
            update_settler_turn.update_settler_turn(1)
            update_game_progress.update_game_progress("game_in_progress")

    settlers = get_settlers.get_settlers()

    knights = get_knights.get_knights()
    print(f"knights: {knights}")

    knights_settler_ids = list(set([knight['settler_id'] for knight in knights]))
    print(f"knights_settler_ids: {knights_settler_ids}")

    list_of_active_knights_by_settler_id = [[knight['level'] for knight in knights if knight['settler_id'] == knight_settler_id and knight['is_active']] for knight_settler_id in knights_settler_ids]
    print(f"list_of_active_knights_by_settler_id: {list_of_active_knights_by_settler_id}")
    
    knight_strength_dict = {knights_settler_ids[i] : sum(list_of_active_knights_by_settler_id[i]) for i in range(len(knights_settler_ids))}
    print(f"knight_strength_dict: {knight_strength_dict}")
    
    for settler in settlers:
        if settler['id'] not in knight_strength_dict:
            knight_strength_dict[settler['id']] = 0 
        
        settler['army_strength'] = 0 if not knight_strength_dict[settler['id']] else knight_strength_dict[settler['id']]
    
    for settler in settlers:
        settler['army_strength'] = knight_strength_dict[settler['id']]     
    
    settlements = get_settlements.get_settlements()

    return render_template('game_page.html', settlers = settlers)