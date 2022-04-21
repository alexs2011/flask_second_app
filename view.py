from flask import render_template

import utilities.utils as utils
from app import app


@app.route('/')
def index() -> str:
    """
    Главная страница со списком всех кандидатов.
    """
    candidates = utils.load_data(utils.FILENAME)
    return render_template("index.html", candidates=candidates)
