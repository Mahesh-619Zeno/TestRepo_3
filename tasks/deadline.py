from datetime import datetime, timedelta, timezone

def set_deadline(task_manager, title, due_date_str, reminder_minutes=None,
                 is_recurring=False, recurrence_pattern=None):
    try:
        due_date = datetime.fromisoformat(due_date_str)
    except ValueError:
        return "Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)."
    if due_date <= datetime.now(timezone.utc):
        return "Error: Due date must be in the future."
    if reminder_minutes and reminder_minutes < 0:
        return "Invalid reminder time."
    task_manager.update_task(
        title,
        due_date=due_date.isoformat(),
        reminder_time=reminder_minutes,
        is_recurring=is_recurring,
        recurrence_pattern=recurrence_pattern,
    )
    return f"Deadline set for task '{title}' on {due_date}."

def remove_deadline(task_manager, title):
    return task_manager.update_task(title, due_date=None, reminder_time=None)

def grant_extension(task_manager, title, user_id, new_due_date_str):
    try:
        new_due_date = datetime.fromisoformat(new_due_date_str)
    except ValueError:
        return "Invalid date format."
    for t in task_manager.tasks:
        if t.title.lower() == title.lower():
            if not t.extended_due_dates:
                t.extended_due_dates = {}
            t.extended_due_dates[user_id] = new_due_date.isoformat()
            task_manager.save_tasks()
            return f"Extended due date for '{title}' granted to user {user_id}."
    return "Task not found."
