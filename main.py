from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority

def main():
    manager = TaskManager()

    while True:
        print("\n=== Task Manager Menu ===")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Update task status")
        print("4. Search tasks")
        print("5. Delete a task")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            priority = input("Enter task priority (High/Medium/Low): ").strip() or "Medium"
            if title:
                manager.add_task(Task(title, description, priority))
                print(f"Task '{title}' added successfully.")
            else:
                print("Invalid title. Task not added.")

        elif choice == "2":
            print("\n--- All Tasks ---")
            for t in manager.list_tasks():
                print(t)

        elif choice == "3":
            title = input("Enter the task title to update: ").strip()
            new_status = input("Enter new status (Pending/In-Progress/Completed): ").strip()
            print(update_status(manager, title, new_status))

        elif choice == "4":
            query = input("Enter search keyword: ").strip()
            results = search_by_title(manager, query)
            print(f"\n--- Search Results for '{query}' ---")
            for t in results:
                print(vars(t))

        elif choice == "5":
            title = input("Enter the title of the task to delete: ").strip()
            if not title:
                print("Invalid input. Title cannot be empty.")
                continue

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
