
import json

DEFAULT_DATA_PATH = "eva-data.json"


def load_eva_data(path=DEFAULT_DATA_PATH):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
