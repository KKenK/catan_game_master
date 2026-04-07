from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from . import db
from .helper_modules import get_game_progress
bp = Blueprint('index_page',__name__)

@bp.route('/')
def index():
    return render_template('index_page.html')

@bp.route('/continue_game')
def continue_game():
  	game_progress = get_game_progress.get_game_progress(db.database_connector)
    
    if game_progress == "game in progress":
        redirect()
    else if game_progress == "settler registeration":
        redirect('/initialise_players/register_settler')
    else if game_progress == "initial settlement placement":
        redirect('/initialise_board/place_settlement')
    else if game_progress == "initial city placement":
        redirect('/initialise_board/place_city')
    else:
        redirect('/')