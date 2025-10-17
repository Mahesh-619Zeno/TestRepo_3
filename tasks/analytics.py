from datetime import datetime, timedelta, timezone

def get_upcoming_deadlines(task_manager, days=7):
    now = datetime.now(timezone.utc)
    upcoming = []
    for t in task_manager.tasks:
        if t.due_date and t.status.lower() != "done":
            due_date = t.due_date if not isinstance(t.due_date, str) else datetime.fromisoformat(t.due_date)
            if now <= due_date <= now + timedelta(days=days):
                upcoming.append({"title": t.title, "due_date": due_date.isoformat()})
    return upcoming if upcoming else [{"message": "No upcoming deadlines"}]
