from flask import (
    Blueprint, g, redirect, render_template, request, url_for
)

from . import db
from .helper_modules import get_settlers, get_resources, update_game_progress
bp = Blueprint('initialise_board', __name__, url_prefix='/initialise_board/')

@bp.route('/place_settlement')
def place_settlement():
    update_game_progress.update_game_progress(db.database_connector, "initial settlement placement")
    settlers = get_settlers.get_settlers(db.database_connector)
    resources = get_resources.get_resources(db.database_connector)
    current_settler = [settler for settler in settlers if settlers.victory_points == 0][0]
    is_last_settler = True if current_settler.id == len(settlers) else False
    return render_template('initalise_board/place_settlement.html',
                            current_settler_name = current_settler['name'],
                            is_last_player = is_last_settler,
                            resources = resources)

@bp.route('/place_city')
def place_city():
    update_game_progress.update_game_progress(db.database_connector, "initial city placement")
    settlers = get_settlers.get_settlers(db.database_connector)
    resources = get_resources(db.database_connector)
    current_settler = [settler for settler in settlers if settlers.victory_points == 1][0] # TODO
    is_last_settler = True if current_settler.id == len(settlers) else False
    return render_template('initalise_board/place_city.html', current_settler = current_settler,
                            is_last_player = is_last_settler,
                            resources = resources)
