from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority
from tasks.task_deadlines import DeadlineTask, DeadlineTaskManager

def main():
    # Existing TaskManager flow
    manager = TaskManager()
    print("=== Welcome to Task Manager ===")

    # Sample flow for iteration 1
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
    deadline_manager.add_task(DeadlineTask(
        title="Submit Invoice",
        description="Submit invoice to client",
        priority="High",
        due_date="2025-10-16",
        reminder_time="10:00",
        recurring="weekly"
    ))
    deadline_manager.add_task(DeadlineTask(
        title="Project Review",
        description="Monthly project review meeting",
        priority="Medium",
        due_date="2025-10-20",
        reminder_time="14:00",
        recurring="monthly"
    ))

    # List all deadline tasks
    print("\n--- All Deadline Tasks ---")
    for t in deadline_manager.list_tasks():
        print(t)

    # Check overdue tasks
    print("\n--- Overdue Deadline Tasks ---")
    overdue = deadline_manager.get_overdue_tasks()
    for t in overdue:
        print(f"- {t.title} (Due: {t.due_date})")

    # Check tasks with reminders now
    print("\n--- Tasks with Reminder Now ---")
    reminders = deadline_manager.check_reminders()
    for t in reminders:
        print(f"- {t.title} (Reminder: {t.reminder_time})")


if __name__ == "__main__":
    main()
