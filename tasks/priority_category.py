# tasks/priority_category.py

from tasks.task import Task, TaskManager

VALID_PRIORITIES = {"Low", "Medium", "High"}

class PriorityCategoryTask(Task):
    def __init__(self, title, description="", priority="Medium", category="Uncategorized", status="Pending"):
        if priority.capitalize() not in VALID_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Valid options: {VALID_PRIORITIES}")
        super().__init__(title, description, priority.capitalize())
        self.category = category
        self.status = status

class PriorityCategoryManager(TaskManager):
    def add_task(self, task: PriorityCategoryTask):
        super().add_task(task)

    def list_tasks(self):
        return [{
            "Title": t.title,
            "Description": t.description,
            "Priority": getattr(t, "priority", "Medium"),
            "Category": getattr(t, "category", "Uncategorized"),
            "Status": t.status
        } for t in self.tasks]

    def filter_by_priority(self, priority):
        priority = priority.capitalize()
        if priority not in VALID_PRIORITIES:
            raise ValueError(f"Priority must be one of {VALID_PRIORITIES}")
        return [t for t in self.tasks if getattr(t, "priority", None) == priority]

    def filter_by_category(self, category):
        return [t for t in self.tasks if getattr(t, "category", None) == category]

    def sort_by_priority(self, descending=True):
        # Map priorities to numeric values for sorting
        priority_map = {"High": 3, "Medium": 2, "Low": 1}
        # Return tasks sorted by priority numeric value
        return sorted(self.tasks, key=lambda t: priority_map.get(getattr(t, "priority", "Medium"), 2), reverse=descending)
