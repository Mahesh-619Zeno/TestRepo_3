# priority_category.py

from tasks.task import Task, TaskManager

class PriorityCategoryManager:
    PRIORITY_ORDER = {"high": 1, "medium": 2, "low": 3}

    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager

    def add_task(self, title, description="", priority="Medium", category="General"):
        # Create a Task with priority and category
        task = Task(title=title, description=description, priority=priority, category=category)
        self.task_manager.add_task(task)

    def list_tasks(self, filter_priority=None, filter_category=None):
        tasks = self.task_manager.tasks
        if filter_priority:
            tasks = [t for t in tasks if t.priority.lower() == filter_priority.lower()]
        if filter_category:
            tasks = [t for t in tasks if t.category.lower() == filter_category.lower()]
        # Sort by priority order
        tasks.sort(key=lambda t: self.PRIORITY_ORDER.get(t.priority.lower(), 4))
        return [{
            "Title": t.title,
            "Description": t.description,
            "Priority": t.priority,
            "Category": t.category,
            "Status": t.status
        } for t in tasks]