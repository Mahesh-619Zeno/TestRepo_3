from tasks.task import Task, TaskManager

VALID_PRIORITIES = {"Low", "Medium", "High"}

class PriorityCategoryTask(Task):
    def __init__(self, title, description="", priority="Medium", category="Uncategorized", status="Pending"):
        if priority.capitalize() not in VALID_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Valid options: {VALID_PRIORITIES}")
        # Initialize base Task with priority assigned
        super().__init__(title, description, priority.capitalize())
        self.category = category
        self.status = status

class PriorityCategoryManager(TaskManager):
    def add_task(self, task: PriorityCategoryTask):
        super().add_task(task)

    def list_tasks(self):
        # Override to include category
        return [{
            "Title": t.title,
            "Description": t.description,
            "Priority": getattr(t, "priority", "Medium"),
            "Category": getattr(t, "category", "Uncategorized"),
            "Status": t.status
        } for t in self.tasks]

    def filter_by_priority(self, priority):
        return [t for t in self.tasks if getattr(t, "priority", None) == priority]

    def filter_by_category(self, category):
        return [t for t in self.tasks if getattr(t, "category", None) == category]