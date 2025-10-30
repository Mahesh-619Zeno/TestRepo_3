import json
import os
import uuid

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")

class Task:
    def __init__(self, title, description="", priority="Medium", user_id=None, shared_with=None, task_id=None):
        self.task_id = task_id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Pending"
        self.user_id = user_id
        self.shared_with = shared_with or []

class TaskManager:
    def __init__(self, current_user):
        self.tasks = []
        self.current_user = current_user
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**d) for d in data]

    def save_tasks(self):
        data = [t.__dict__ for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def add_task(self, task):
        if self.current_user.role == "User":
            task.user_id = self.current_user.user_id
        self.tasks.append(task)
        self.save_tasks()
        return f"Task '{task.title}' added."

    def list_tasks(self):
        if self.current_user.role == "Admin":
            return [self._task_dict(t) for t in self.tasks]
        return [
            self._task_dict(t)
            for t in self.tasks
            if t.user_id == self.current_user.user_id or self.current_user.user_id in t.shared_with
        ]

    def _task_dict(self, t):
        return {
            "ID": t.task_id,
            "Title": t.title,
            "Owner": t.user_id,
            "Priority": t.priority,
            "Status": t.status,
            "SharedWith": t.shared_with
        }

    def share_task(self, task_id, share_with_user_id):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if not task:
            return "Task not found."
        if task.user_id != self.current_user.user_id and self.current_user.role != "Admin":
            return "Permission denied. Only owner or Admin can share."
        if share_with_user_id not in task.shared_with:
            task.shared_with.append(share_with_user_id)
            self.save_tasks()
            return f"Task '{task.title}' shared successfully."
        return "User already has access."