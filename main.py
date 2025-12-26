from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority
from tasks.reminder import reminder_service
from threading import Thread

def print_dashboard(task_manager):
    summary = task_manager.get_dashboard_summary()
    print("\n=== Dashboard Summary ===")
    for k, v in summary.items():
        print(f"{k}: {v}")

def print_task_list(tasks):
    print("\n--- Tasks ---")
    for t in tasks:
        print(f"Title: {t.title} | Description: {t.description} | Priority: {t.priority} | Status: {t.status} | Deadline: {t.deadline}")

def main():
    manager = TaskManager()
    print("=== Welcome to Task Manager with Deadlines and Reminders ===")

    # Add sample tasks (with deadlines in "YYYY-MM-DD HH:MM" format)
    if len(manager.tasks) == 0:
        manager.add_task(Task("Finish Report", "Complete the financial report", "High", "2025-10-17 17:00"))
        manager.add_task(Task("Email Client", "Send project updates", "Medium", "2025-10-18 12:00"))
        manager.add_task(Task("Team Meeting", "Discuss project roadmap", "Low", "2025-10-16 15:00"))

    # List all tasks
    print_task_list(manager.tasks)

    # Show dashboard summary widget
    print_dashboard(manager)

    # Update status example
    print("\n--- Update Status ---")
    print(update_status(manager, "Finish Report", "In-Progress"))

    # Search tasks
    print("\n--- Search by Title 'Team' ---")
    results = search_by_title(manager, "Team")
    print_task_list(results)

    # Launch reminder service in background thread
    reminder_thread = Thread(target=reminder_service, args=(manager,), daemon=True)
    reminder_thread.start()

    # Interactive loop to allow adding tasks with deadlines (simple CLI)
    while True:
        print("\nOptions:\n1. Add Task\n2. List Tasks\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            priority = input("Priority (Low/Medium/High): ")
            deadline = input("Deadline (YYYY-MM-DD HH:MM) or leave blank for no deadline: ")
            deadline = deadline if deadline else None
            manager.add_task(Task(title, description, priority, deadline))
            print("Task added.")
        elif choice == "2":
            print_task_list(manager.tasks)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
