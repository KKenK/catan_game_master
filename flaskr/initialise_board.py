# place_settlement.py
from flask import (
    Blueprint, g, redirect, render_template, request, url_for
)

from . import db
from . import get_players, get_resources

bp = Blueprint('initialise_board', __name__, url_prefix='/initialise_board/')

@bp.route('/place_settlement')
def place_settlement():
  	players = get_players(db.database_connector)
    resources = get_resources(db.database_connector)
  	current_player = [player for players if player.victory_points == 0][0]
    is_last_player = current_player.id == len(players)
    return render_template('initalise_board/place_settlement.html', current_player = current_player, is_last_player = is_last_player, resources = resources)

@bp.route('/place_city')
def place_city():
  	players = get_players(db.database_connector)
    resources = get_resources(db.database_connector)
  	current_player = [player for players if player.victory_points == 1][0]
    is_last_player = current_player.id == len(players)
    return render_template('initalise_board/place_city.html', current_player = current_player, is_last_player = is_last_player, resources = resources)

# get_first_player_without_settlement.py
def get_first_player_without_settlement(database_connector):
    with databse_connector() as db:
    	return db.execute("""SELECT * FROM settlers WHERE victory_points = 0 LIMIT 1""").fetchone()

def get_last_player_without_city(database_connector):
    with databse_connector() as db:
    	return db.execute("""SELECT * FROM settlers WHERE victory_points = 1 ORDER BY id DESC LIMIT 1""").fetchone()

def get_players(database_connector):
    with databse_connector() as db:
    	return db.execute("""SELECT * FROM settlers""").fetchall()

def get_resources(database_connector):
    with databse_connector() as db:
    	return db.execute("""SELECT * FROM resources""").fetchall()
      
# place_settlement.html
{% extends "layout.html" %}

    {% block body %}
        <header>
            <h1>{{player_name}} place settlement!</h1>
        </header>
        <main>
            <form action="place_settlement" method="post">
        		<div>
            		<label for="roll_1"> Roll 1: </label>
					<select id="roll_1" name="roll_1">
                		<option value="">None</option>
                		{% for resource in resources %}
                  			<option value="{{resource}}">{{resource}}</option>
                  		{% endfor %}
                	</selct>
                </div>
            </form>
        </main>
    {% endblock %}