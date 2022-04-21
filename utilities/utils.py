import json

FILENAME = r"./data/candidates.json"


def load_data(filename: str) -> list[dict]:
    """
    Загружает данные из файла формата JSON.
    """
    with open(filename, 'r', encoding='utf-8') as f_in:
        return json.load(f_in)


def get_candidate_by_uid(candidates: list[dict], uid: int) -> dict:
    """
    Поиск кандидата по uid.
    """
    for candidate in candidates:
        if candidate.get("id") == uid:
            return candidate
    raise ValueError(f"ValueError: Кандидат с uid={uid} не найден.")


def get_candidates_by_skill(candidates: list[dict], skill: str) -> list[dict]:
    """
    Поиск всех кандидатов, у которых есть навык skill.
    """
    res = []
    for candidate in candidates:
        skills = candidate.get("skills").lower().split(", ")
        if skill.lower() in skills:
            res.append(candidate)
    return res


def get_candidates_by_name(candidates: list[dict], name: str) -> list[dict]:
    """
    Поиск всех кандидатов с именем name.
    """
    res = []
    for candidate in candidates:
        name_lst = candidate.get("name").lower().split()
        if name.lower() in name_lst:
            res.append(candidate)
    return res
