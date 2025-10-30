def delete_task(task_manager, title):
    for t in task_manager.tasks:
        if t.title.lower() == title.lower():
            task_manager.tasks.remove(t)
            task_manager.save_tasks()
            return f"Task '{t.title}' has been deleted successfully."
    return f"Task '{title}' not found."
