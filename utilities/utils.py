import json

FILENAME = r"./data/candidates.json"


def load_data(filename: str) -> list[dict]:
    """
    Загружает данные из файла формата JSON.
    """
    with open(filename, 'r', encoding='utf-8') as f_in:
        return json.load(f_in)
