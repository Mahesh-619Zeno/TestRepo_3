# tasks/filter_sort.py

PRIORITY_VALUES = {"High": 3, "Medium": 2, "Low": 1}

def filter_by_priority(task_manager, priority):
    valid_priorities = [p.lower() for p in PRIORITY_VALUES.keys()]
    if priority.lower() not in valid_priorities:
        return f"Invalid priority '{priority}'. Valid options: High, Medium, Low."
    results = [t for t in task_manager.tasks if t.priority.lower() == priority.lower()]
    if not results:
        return f"No tasks found for priority '{priority}'."
    return results

def filter_by_category(task_manager, category):
    results = [t for t in task_manager.tasks if t.category.lower() == category.lower()]
    if not results:
        return f"No tasks found for category '{category}'."
    return results

def sort_by_priority(task_manager):
    if not task_manager.tasks:
        return "No tasks to sort."
    sorted_tasks = sorted(
        task_manager.tasks,
        key=lambda t: PRIORITY_VALUES.get(t.priority.capitalize(), 0),
        reverse=True
    )
    return sorted_tasks
