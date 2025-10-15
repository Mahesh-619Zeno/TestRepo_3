# Updated to find and update task respecting user ownership/admin access

def update_status(task_manager, title, new_status, user_id=None, admin=False):
    for t in task_manager.tasks:
        if t.title.lower() == title.lower():
            # Only update if user is owner or admin
            if admin or t.owner_id == user_id:
                t.status = new_status
                task_manager.save_tasks()
                return f"Task '{t.title}' status updated to '{new_status}'."
            else:
                return "You do not have permission to update this task."
    return f"Task '{title}' not found."
