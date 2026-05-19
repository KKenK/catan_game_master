from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from .helper_modules import get_game_progress, get_settlers, get_knights, get_settlements, update_game_progress

bp = Blueprint('game_in_progress',__name__, url_prefix='/game')

@bp.route('/')
def game():
    
    if get_game_progress.get_game_progress() != "game_in_progress":
            update_game_progress.update_settler_turn(1)
            update_game_progress.update_game_progress("game_in_progress")

    settlers = get_settlers.get_settlers()

    knights = get_knights.get_knights()
        
    settlements = get_settlements.get_settlements()

    return render_template('game_page.html')