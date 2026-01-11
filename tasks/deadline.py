from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M"

def parse_due_date(date_str):
    """Validates and converts user input into ISO 8601 string."""
    try:
        due = datetime.strptime(date_str, DATE_FORMAT)
        if due < datetime.now():
            return None, "Due date cannot be in the past."
        return due.isoformat(), None
    except ValueError:
        return None, f"Invalid format. Expected 'YYYY-MM-DD HH:MM'."

def add_or_update_due_date(task_manager, title, new_due_date_str):
    task = task_manager.get_task(title)
    if not task:
        return f"Task '{title}' not found."
    if not new_due_date_str:
        task.due_date = None
        task_manager.save_tasks()
        return f"Due date removed from task '{title}'."
    iso_date, err = parse_due_date(new_due_date_str)
    if err:
        return f"Error: {err}"
    task.due_date = iso_date
    task_manager.save_tasks()
    return f"Task '{title}' due date set to {new_due_date_str}."