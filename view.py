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


@app.route('/skill/<skill>')
def search_by_skill(skill: str) -> str:
    """
    Страница с информацией о тех кандидатах, у которых есть навык skill.
    """
    candidates = utils.load_data(utils.FILENAME)
    filtered_candidates = utils.get_candidates_by_skill(candidates, skill)
    return render_template("search_by_skill.html", candidates=filtered_candidates, skill=skill)
