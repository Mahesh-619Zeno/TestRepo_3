import json
import os
from typing import List, Optional

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")


class Task:
    def __init__(self, title: str, description: str = "", priority: str = "Medium", status: str = "Pending"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status  # "Pending", "In Progress", "Completed"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict) -> 'Task':
        return Task(
            title=data.get("title", ""),
            description=data.get("description", ""),
            priority=data.get("priority", "Medium"),
            status=data.get("status", "Pending")
        )


class TaskManager:
    def __init__(self, data_file: Optional[str] = None):
        self.data_file = data_file or DATA_FILE
        self.tasks: List[Task] = []
        self.load_tasks()

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            raise ValueError("Only Task instances can be added.")
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self) -> List[dict]:
        return [task.to_dict() for task in self.tasks]

    def save_tasks(self):
        try:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(item) for item in data]
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
