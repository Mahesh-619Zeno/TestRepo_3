from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority
from tasks.reminder import reminder_service
from threading import Thread

def main():
    manager = TaskManager()
    print("=== Welcome to Task Manager with Deadlines ===")

    # Add sample tasks with deadlines (format: YYYY-MM-DD HH:MM)
    manager.add_task(Task("Finish Report", "Complete the financial report", "High", "2025-10-17 17:00"))
    manager.add_task(Task("Email Client", "Send project updates", "Medium", "2025-10-18 12:00"))
    manager.add_task(Task("Team Meeting", "Discuss project roadmap", "Low", "2025-10-16 15:00"))
    
    # List all tasks
    print("\n--- All Tasks ---")
    for t in manager.list_tasks():
        print(t)

    # Update status example
    print("\n--- Update Status ---")
    print(update_status(manager, "Finish Report", "In-Progress"))

    # Search tasks by title
    print("\n--- Search by Title 'Team' ---")
    results = search_by_title(manager, "Team")
    for t in results:
        print(vars(t))

    # Start reminder service in background thread
    reminder_thread = Thread(target=reminder_service, args=(manager,), daemon=True)
    reminder_thread.start()

    # Keep main thread alive for demonstration, or implement CLI/menu as needed
    input("\nPress Enter to exit...\n")

if __name__ == "__main__":
    main()
