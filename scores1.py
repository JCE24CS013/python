import json
def save_scores(dictonary):
    with open("scores.json", "w") as file:
        json.dump(dictonary, file, indent=2)