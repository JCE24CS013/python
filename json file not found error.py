import json
def load_json_safe(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except Exception:
        print("Invalid JSON data.")
        return None