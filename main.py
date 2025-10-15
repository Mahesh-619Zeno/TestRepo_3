from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title
from tasks.reminder import reminder_service
from threading import Thread

def print_dashboard(manager):
    summary = manager.get_dashboard_summary()
    print("\n=== Dashboard Summary ===")
    for k, v in summary.items():
        print(f"{k}: {v}")

def print_tasks(tasks):
    print("\n--- Task List ---")
    for t in tasks:
        print(f"Title: {t.title} | Desc: {t.description} | Priority: {t.priority} | Status: {t.status} | Deadline: {t.deadline}")

def main():
    manager = TaskManager()

    print("Welcome to Task Manager with Deadlines & Notifications")

    if len(manager.tasks) == 0:
        manager.add_task(Task("Finish Report", "Complete financial report", "High", "2025-10-17 17:00"))
        manager.add_task(Task("Email Client", "Send project updates", "Medium", "2025-10-18 12:00"))
        manager.add_task(Task("Team Meeting", "Discuss roadmap", "Low", "2025-10-16 15:00"))

    print_tasks(manager.tasks)
    print_dashboard(manager)

    print("\n-- Update Example --")
    print(update_status(manager, "Finish Report", "In-Progress"))

    print("\n-- Search by Title 'Team' --")
    results = search_by_title(manager, "Team")
    print_tasks(results)

    # Start reminder service in background thread
    Thread(target=reminder_service, args=(manager,), daemon=True).start()

    while True:
        print("\nOptions:\n1. Add Task\n2. List Tasks\n3. Dashboard\n4. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            title = input("Title: ").strip()
            desc = input("Description: ").strip()
            priority = input("Priority (Low/Medium/High): ").strip()
            deadline = input("Deadline (YYYY-MM-DD HH:MM) or leave blank: ").strip() or None
            manager.add_task(Task(title, desc, priority, deadline))
            print("Task added.")
        elif choice == "2":
            print_tasks(manager.tasks)
        elif choice == "3":
            print_dashboard(manager)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
