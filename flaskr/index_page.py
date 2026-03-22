from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)
from . import db

bp = Blueprint('index_page',__name__)

@bp.route('/')
def index():
    return render_template('index_page.html')
