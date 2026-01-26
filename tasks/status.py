def update_status(task_manager, title, new_status):
    valid_statuses = {"Pending", "In Progress", "Completed", "On Hold"}

    if new_status not in valid_statuses:
        return f"Invalid status '{new_status}'. Allowed: {', '.join(valid_statuses)}"

    for task in task_manager.tasks:
        if task.title.strip().lower() == title.strip().lower():
            if task.status == new_status:
                return f"Task '{task.title}' is already marked as '{new_status}'."
            task.status = new_status
            task_manager.save_tasks()
            return f"Task '{task.title}' status updated to '{new_status}'."

    return f"Task '{title}' not found."
