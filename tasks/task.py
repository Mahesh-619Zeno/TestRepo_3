import json
import os
from typing import List
from dataclasses import dataclass, asdict

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")


@dataclass
class Task:
    title: str
    description: str = ""
    priority: str = "Medium"
    status: str = "Pending"  # Default status


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self.load_tasks()

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self) -> List[dict]:
        return [asdict(t) for t in self.tasks]

    def save_tasks(self) -> None:
        try:
            os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump([asdict(t) for t in self.tasks], f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self) -> None:
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.tasks = [Task(**d) for d in data]
            except Exception as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
