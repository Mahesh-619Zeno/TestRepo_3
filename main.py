from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority

def main():
    manager = TaskManager()
    print("=== Welcome to Task Manager ===")

    while True:
        print("\n--- Main Menu ---")
        print("1. Add a task")
        print("2. List all tasks")
        print("3. Update task status")
        print("4. Search tasks")
        print("5. Delete a task")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter title: ").strip()
            desc = input("Enter description: ").strip()
            priority = input("Enter priority (Low/Medium/High): ").strip() or "Medium"
            if title:
                manager.add_task(Task(title, desc, priority))
                print(f"Task '{title}' added successfully.")
            else:
                print("Title cannot be empty.")

        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks available.")
            else:
                for t in tasks:
                    print(t)

        elif choice == "3":
            title = input("Enter the title of the task to update: ").strip()
            new_status = input("Enter new status (Pending/In-Progress/Completed): ").strip()
            print(update_status(manager, title, new_status))

        elif choice == "4":
            query = input("Search by title keyword: ").strip()
            results = search_by_title(manager, query)
            if results:
                for t in results:
                    print(vars(t))
            else:
                print("No matching tasks found.")

        elif choice == "5":
            title = input("Enter the title of the task to delete: ").strip()
            if not title:
                print("Invalid input. Task title cannot be empty.")
            else:
                deleted = manager.delete_task(title)
                if deleted:
                    print(f"Task '{title}' deleted successfully.")
                else:
                    print(f"Task with title '{title}' not found.")

        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")