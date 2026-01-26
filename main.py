from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority
from tasks.deadline_reminder import DeadlineReminderManager

def main():
    manager = TaskManager()
    reminder_mgr = DeadlineReminderManager(manager)

    print("=== Task Manager with Deadlines and Reminders ===")

    manager.add_task(Task("Finish Report", "Complete financial report", "High"))
    manager.add_task(Task("Email Client", "Send project updates", "Medium"))
    manager.add_task(Task("Team Meeting", "Discuss project roadmap", "Low"))

    response = reminder_mgr.set_deadline("Finish Report", "2025-10-20T15:00:00", reminder_minutes=60)
    print(response)

    reminder_mgr.start_scheduler()

    print("\n--- Listing Tasks ---")
    for t in manager.tasks:
        print(vars(t))

    import time
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        reminder_mgr.stop_scheduler()
        print("Scheduler stopped.")

if __name__ == "__main__":
    main()