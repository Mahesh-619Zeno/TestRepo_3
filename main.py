import argparse
from tasks.priority_category import PriorityCategoryTask, PriorityCategoryManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority  # use existing functions as-is

def valid_priority(value):
    valid = {"Low", "Medium", "High"}
    if value.capitalize() not in valid:
        raise argparse.ArgumentTypeError(f"Priority must be one of {valid}")
    return value.capitalize()

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    parser.add_argument('--add', action='store_true', help='Add a new task')
    parser.add_argument('--title', type=str, help='Task title for adding')
    parser.add_argument('--description', type=str, default="", help='Task description for adding')
    parser.add_argument('--priority', type=valid_priority, default="Medium", help="Priority: Low, Medium, or High")
    parser.add_argument('--category', type=str, default="Uncategorized", help='Category for the task')
    parser.add_argument('--list', action='store_true', help='List all tasks')

    args = parser.parse_args()

    manager = PriorityCategoryManager()

    if args.add:
        if not args.title:
            print("Error: --title is required to add a task.")
            return
        try:
            task = PriorityCategoryTask(
                title=args.title,
                description=args.description,
                priority=args.priority,
                category=args.category
            )
            manager.add_task(task)
            print(f"Task '{args.title}' added with priority '{args.priority}' and category '{args.category}'.")
        except ValueError as ve:
            print(f"Error: {ve}")
            return

    if args.list:
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print(f"{'Title':<20} {'Priority':<8} {'Category':<15} {'Status':<12} Description")
            print("-" * 70)
            for t in tasks:
                print(f"{t['Title']:<20} {t['Priority']:<8} {t['Category']:<15} {t['Status']:<12} {t['Description']}")

if __name__ == "__main__":
    main()