import json
def load_scores():
    try:
        with open("scores.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}