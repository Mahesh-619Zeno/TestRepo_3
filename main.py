# main.py

from tasks.task import TaskManager
from priority_category import PriorityCategoryManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority

def main():
    manager = TaskManager()
    pc_manager = PriorityCategoryManager(manager)

    print("=== Welcome to Task Manager with Prioritization and Categorization ===")

    # Add some sample tasks with priority and category using priority_category manager
    pc_manager.add_task("Finish Report", "Complete the financial report", "High", "Work")
    pc_manager.add_task("Email Client", "Send project updates", "Medium", "Communication")
    pc_manager.add_task("Team Meeting", "Discuss project roadmap", "Low", "Meeting")

    # List all tasks sorted by priority and include category
    print("\n--- All Tasks Sorted by Priority ---")
    for t in pc_manager.list_tasks():
        print(t)

    # Update status using existing status module on one task
    print("\n--- Update Status ---")
    print(update_status(manager, "Finish Report", "In-Progress"))

    # Search tasks by title using existing search module
    print("\n--- Search by Title 'Team' ---")
    results = search_by_title(manager, "Team")
    for t in results:
        print(vars(t))

    # Demonstrate filtering tasks by priority via priority_category manager
    print("\n--- High Priority Tasks ---")
    for t in pc_manager.list_tasks(filter_priority="High"):
        print(t)

    # Demonstrate filtering tasks by category via priority_category manager
    print("\n--- Tasks in Category 'Work' ---")
    for t in pc_manager.list_tasks(filter_category="Work"):
        print(t)

if __name__ == "__main__":
    main()
