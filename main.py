# main.py

from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority
from tasks.filter_sort import filter_by_priority, filter_by_category, sort_by_priority

def main():
    manager = TaskManager()
    print("=== Welcome to Task Manager ===")

    # Sample tasks
    try:
        manager.add_task(Task("Finish Report", "Complete financial report", "High", "Work"))
        manager.add_task(Task("Email Client", "Send project updates", "Medium", "Work"))
        manager.add_task(Task("Yoga Session", "Morning exercise", "Low", "Personal"))
    except ValueError as e:
        print(f"Task creation error: {e}")

    # List all tasks
    print("\n--- All Tasks ---")
    all_tasks = manager.list_tasks()
    if isinstance(all_tasks, str):
        print(all_tasks)
    else:
        for t in all_tasks:
            print(t)

    # Filter by priority
    print("\n--- Filter by Priority: High ---")
    results = filter_by_priority(manager, "High")
    if isinstance(results, str):
        print(results)
    else:
        for t in results:
            print(vars(t))

    # Filter by category
    print("\n--- Filter by Category: Work ---")
    results = filter_by_category(manager, "Work")
    if isinstance(results, str):
        print(results)
    else:
        for t in results:
            print(vars(t))

    # Sort by priority
    print("\n--- Sorted by Priority ---")
    results = sort_by_priority(manager)
    if isinstance(results, str):
        print(results)
    else:
        for t in results:
            print(vars(t))

if __name__ == "__main__":
    main()
