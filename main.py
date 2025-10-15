from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority
from tasks.task_deadlines import DeadlineTask, DeadlineTaskManager
from datetime import datetime, timedelta

def main():
    # Existing TaskManager flow
    manager = TaskManager()
    print("=== Welcome to Task Manager ===")

    # Sample tasks
    manager.add_task(Task("Finish Report", "Complete the financial report", "High"))
    manager.add_task(Task("Email Client", "Send project updates", "Medium"))
    manager.add_task(Task("Team Meeting", "Discuss project roadmap", "Low"))

    print("\n--- All Tasks ---")
    for t in manager.list_tasks():
        print(t)

    print("\n--- Update Status ---")
    print(update_status(manager, "Finish Report", "In-Progress"))

    print("\n--- Search by Title 'Team' ---")
    results = search_by_title(manager, "Team")
    for t in results:
        print(vars(t))

    # New TaskDeadlines flow
    deadline_manager = DeadlineTaskManager()
    print("\n=== Task Deadlines and Reminder System ===")

    # Add sample deadline tasks
    now = datetime.now()
    deadline_manager.add_task(DeadlineTask(
        title="Submit Invoice",
        description="Submit invoice to client",
        priority="High",
        due_date=(now + timedelta(days=1)).strftime("%Y-%m-%d"),
        due_time=(now + timedelta(hours=2)).strftime("%H:%M"),
        reminder_time=60,  # 60 minutes before
        is_recurring=True,
        recurrence_pattern={"frequency": "weekly", "interval": 1}
    ))

    deadline_manager.add_task(DeadlineTask(
        title="Project Review",
        description="Monthly project review meeting",
        priority="Medium",
        due_date=(now + timedelta(days=3)).strftime("%Y-%m-%d"),
        due_time="14:00",
        reminder_time=120,  # 2 hours before
        is_recurring=True,
        recurrence_pattern={"frequency": "monthly", "interval": 1}
    ))

    # List all deadline tasks sorted by due date
    print("\n--- All Deadline Tasks Sorted by Due Date ---")
    for t in deadline_manager.list_tasks(sort_by_due=True):
        print(t)

    # Check overdue tasks
    print("\n--- Overdue Deadline Tasks ---")
    overdue = deadline_manager.check_overdue()
    for t in overdue:
        print(f"- {t.title} (Due: {t.due_date} {t.due_time})")

    # Check tasks with reminders now
    print("\n--- Tasks with Upcoming Reminders ---")
    reminders = deadline_manager.get_upcoming_reminders()
    for t in reminders:
        print(f"- {t.title} (Due: {t.due_date} {t.due_time}, Reminder: {t.reminder_time} mins before)")

    # Update recurring tasks whose deadlines have passed
    deadline_manager.update_recurring_tasks()
    print("\n--- Recurring Tasks Updated ---")
    for t in deadline_manager.list_tasks(sort_by_due=True):
        print(t)


if __name__ == "__main__":
    main()
