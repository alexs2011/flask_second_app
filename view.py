from flask import render_template, abort

import utilities.utils as utils
from app import app


@app.route('/')
def index() -> str:
    """
    Главная страница со списком всех кандидатов.
    """
    candidates = utils.load_data(utils.FILENAME)
    return render_template("index.html", candidates=candidates)


@app.route('/candidate/<int:uid>')
def candidate_profile(uid: int) -> str:
    """
    Страница профиля кандидата.
    """
    candidates = utils.load_data(utils.FILENAME)
    try:
        candidate = utils.get_candidate_by_uid(candidates, uid)
    except ValueError as e:  # Если нет кандидата с данным uid.
        print(e)
        abort(404)
    return render_template("candidate.html", candidate=candidate)
