import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = response.json()
completed_todos = []
for todo in todos:
    if todo["completed"] == True:
        completed_todos.append(todo)
with open("completed_todos.json", "w") as file:
    json.dump(completed_todos, file, indent=4)
print("Completed todos saved successfully!")