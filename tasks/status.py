def update_status(task_manager, title, new_status, user_can_edit=True):
    if not user_can_edit:
        return "Permission denied to update task status."
    for t in task_manager.tasks:
        if t.title.lower() == title.lower():
            if task_manager.current_user.role != "Admin" and t.user_id != task_manager.current_user.user_id:
                return "Permission denied: cannot update status of another user's task."
            t.status = new_status
            task_manager.save_tasks()
            return f"Task '{t.title}' status updated to '{new_status}'."
    return f"Task '{title}' not found."
