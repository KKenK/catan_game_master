from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from . import db
from .helper_modules import get_game_progress, clear_game_tables, get_settlers
bp = Blueprint('index_page',__name__)

@bp.route('/')
def index():
    return render_template('index_page.html')

@bp.route('/new_game')
def new_game():
    #clear_game_tables.clear_game_tables(db.DatabaseConnector)
    print(get_settlers.get_settlers(db.DatabaseConnector))   
    return redirect("/initialise_players/register_settlers")

@bp.route('/continue_game')
def continue_game():
    game_progress = get_game_progress.get_game_progress(db.DatabaseConnector)
    
    if game_progress == "game in progress":
        return redirect()
    elif game_progress == "settler registeration":
        return redirect('/initialise_players/register_settler')
    elif game_progress == "initial settlement placement":
        return redirect('/initialise_board/place_settlement')
    elif game_progress == "initial city placement":
        return redirect('/initialise_board/place_city')
    else:
        return redirect('/')