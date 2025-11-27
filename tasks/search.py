def search_by_title(task_manager, query):
    return [t for t in task_manager.tasks if query.lower() in t.title.lower() and 
            (task_manager.current_user.role == "Admin" or t.user_id == task_manager.current_user.user_id)]

def search_by_priority(task_manager, priority):
    return [t for t in task_manager.tasks if t.priority.lower() == priority.lower() and 
            (task_manager.current_user.role == "Admin" or t.user_id == task_manager.current_user.user_id)]

def search_by_due_date(task_manager, ascending=True):
    tasks = [t for t in task_manager.tasks if (task_manager.current_user.role == "Admin" or t.user_id == task_manager.current_user.user_id)]
    def due_date_key(t):
        dt = t.get_due_datetime(task_manager.current_user.user_id)
        from datetime import datetime
        return dt if dt else datetime.max.replace(tzinfo=None)
    tasks.sort(key=due_date_key, reverse=not ascending)
    return tasks
