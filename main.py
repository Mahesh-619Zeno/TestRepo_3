from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority

def main():
    manager = TaskManager()
    print("=== Welcome to Task Manager ===")

    # Sample flow for iteration 1
    # Add sample tasks
    manager.add_task(Task("Finish Report", "Complete the financial report", "High"))
    manager.add_task(Task("Email Client", "Send project updates", "Medium"))
    manager.add_task(Task("Team Meeting", "Discuss project roadmap", "Low"))
    
    parser.add_argument('--filter-priority', type=str, help='Filter tasks by priority')
    parser.add_argument('--filter-category', type=str, help='Filter tasks by category')
    parser.add_argument('--sort-priority', action='store_true', help='Sort tasks by priority')
    args = parser.parse_args()

    # List all tasks
    print("\n--- All Tasks ---")
    for t in manager.list_tasks():
        print(t)

    # Update status
    print("\n--- Update Status ---")
    print(update_status(manager, "Finish Report", "In-Progress"))

    # Search tasks
    print("\n--- Search by Title 'Team' ---")
    results = search_by_title(manager, "Team")
    for t in results:
        print(vars(t))

    if args.filter_priority:
        try:
            filtered = manager.filter_by_priority(args.filter_priority)
            print(f"Tasks filtered by priority '{args.filter_priority}':")
            for t in filtered:
                print(vars(t))
        except ValueError as ve:
            print(f"Error: {ve}")

    if args.filter_category:
        filtered = manager.filter_by_category(args.filter_category)
        print(f"Tasks filtered by category '{args.filter_category}':")
        for t in filtered:
            print(vars(t))

    if args.sort_priority:
        sorted_tasks = manager.sort_by_priority()
        print("Tasks sorted by priority (High to Low):")
        for t in sorted_tasks:
            print(vars(t))

if __name__ == "__main__":
    main()
