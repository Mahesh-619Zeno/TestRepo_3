import argparse
from tasks.priority_category import PriorityCategoryTask, PriorityCategoryManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority

def valid_priority(value):
    valid = {"Low", "Medium", "High"}
    if value.capitalize() not in valid:
        raise argparse.ArgumentTypeError(f"Priority must be one of {valid}")
    return value.capitalize()

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    parser.add_argument('--add', action='store_true', help='Add a new task')
    parser.add_argument('--title', type=str, help='Task title')
    parser.add_argument('--description', type=str, default="", help='Task description')
    parser.add_argument('--priority', type=valid_priority, default="Medium", help='Task priority')
    parser.add_argument('--category', type=str, default="Uncategorized", help='Task category')
    parser.add_argument('--list', action='store_true', help='List all tasks')
    parser.add_argument('--filter-priority', type=str, help='Filter tasks by priority')
    parser.add_argument('--filter-category', type=str, help='Filter tasks by category')
    parser.add_argument('--sort-priority', action='store_true', help='Sort tasks by priority High to Low')

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
        except ValueError as e:
            print(f"Error: {e}")
            return

    if args.list:
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print(f"{'Title':<20} {'Priority':<8} {'Category':<15} {'Status':<12} Description")
            print("-" * 80)
            for t in tasks:
                print(f"{t['Title']:<20} {t['Priority']:<8} {t['Category']:<15} {t['Status']:<12} {t['Description']}")

    if args.filter_priority or args.filter_category:
        try:
            filtered = manager.filter_tasks(priority=args.filter_priority, category=args.filter_category)
            if not filtered:
                print("No matching tasks found for the given filter(s).")
            else:
                print(f"Filtered tasks:")
                for t in filtered:
                    print(vars(t))
        except ValueError as ve:
            print(f"Error: {ve}")

    if args.sort_priority:
        sorted_tasks = manager.sort_by_priority()
        if not sorted_tasks:
            print("No tasks to display after sorting.")
        else:
            print("Tasks sorted by priority (High to Low):")
            for t in sorted_tasks:
                print(vars(t))

if __name__ == "__main__":
    main()
