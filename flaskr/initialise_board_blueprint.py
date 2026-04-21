from flask import (
    Blueprint, g, redirect, render_template, request, url_for
)

from .helper_modules import get_settlers, get_resources, update_game_progress
bp = Blueprint('initialise_board', __name__, url_prefix='/initialise_board/')

@bp.route('/place_settlement')
def place_settlement():
    update_game_progress.update_game_progress("initial settlement placement")
    settlers = get_settlers.get_settlers()
    resources = get_resources.get_resources()
    current_settler = [settler for settler in settlers if settlers.victory_points == 0][0]
    have_all_settlers_placed_a_settlement = True if current_settler.id == len(settlers) else False
    return render_template('initalise_board/place_settlement.html', current_settler_name = current_settler['name'],
                            have_all_settlers_placed_a_settlement = have_all_settlers_placed_a_settlement,
                            resources = resources)

@bp.route('/place_city')
def place_city():
    update_game_progress.update_game_progress("initial city placement")
    settlers = get_settlers.get_settlers()
    resources = get_resources()
    current_settler = [settler for settler in settlers if settlers.victory_points == 1][-1]
    have_all_settlers_placed_a_city = True if current_settler.id == len(settlers) else False
    return render_template('initalise_board/place_city.html', current_settler_name = current_settler['name'],
                            have_all_settlers_placed_a_city = have_all_settlers_placed_a_city,
                            resources = resources)