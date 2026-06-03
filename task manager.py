import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


class Task:
    def __init__(self, id, title, priority="medium", due=None):
        self.id = id
        self.title = title
        self.priority = priority
        self.due = due
        self.completed = False

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "due": self.due,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            data["id"],
            data["title"],
            data.get("priority", "medium"),
            data.get("due")
        )
        task.completed = data.get("completed", False)
        return task


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load()

    def add(self, title, priority="medium", due=None):
        task = Task(self.next_id, title, priority, due)
        self.tasks.append(task)
        self.next_id += 1
        self.save()
        print("Task added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nTASK LIST")
        print("-" * 50)

        for task in self.tasks:
            status = "Done" if task.completed else "Pending"

            print(
                f"ID: {task.id} | "
                f"Title: {task.title} | "
                f"Priority: {task.priority} | "
                f"Due: {task.due} | "
                f"Status: {status}"
            )

    def complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self.save()
                print("Task marked as completed.")
                return

        print("Task not found.")

    def delete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save()
                print("Task deleted successfully.")
                return

        print("Task not found.")

    def save(self):
        data = [task.to_dict() for task in self.tasks]

        with open(TASKS_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def load(self):
        if not os.path.exists(TASKS_FILE):
            return

        with open(TASKS_FILE, "r") as file:
            data = json.load(file)

        self.tasks = [Task.from_dict(item) for item in data]

        if self.tasks:
            self.next_id = max(task.id for task in self.tasks) + 1


def main():
    manager = TaskManager()

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter priority (low/medium/high): ")
            due = input("Enter due date (YYYY-MM-DD) or leave blank: ")

            if due == "":
                due = None

            manager.add(title, priority, due)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            manager.complete(task_id)

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            manager.delete(task_id)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()