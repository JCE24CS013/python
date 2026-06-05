import json
task_file ="tasks.json"
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("tasks.json not found. Starting with an empty task list.")
        return []
    except Exception:
        print("tasks.json is corrupted. Starting with an empty task list.")
        return []