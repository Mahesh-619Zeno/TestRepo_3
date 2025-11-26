from users.user_manager import UserManager
from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title
from tasks.notifications import NotificationService

def show_main_menu(user):
    print(f"\n=== Task Manager ===")
    print(f"Logged in as: {user.username} ({user.role})")
    print("\n-- Main Menu --")
    print("1. List Tasks")
    print("2. Add Task")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Search Task by Title")
    print("6. Switch User")
    if user.role == "Admin":
        print("7. Manage Users")
    print("0. Logout and Exit")

def handle_admin_user_management(um, current_username):
    while True:
        print("\n-- Admin User Management --")
        print("1. Add User")
        print("2. Remove User")
        print("3. List Users")
        print("0. Back")
        choice = input("Select: ").strip()
        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            role = input("Role (Admin/User): ").strip()
            print(um.add_user(username, password, role))
        elif choice == "2":
            username = input("Username to remove: ").strip()
            print(um.remove_user(username, current_username))
        elif choice == "3":
            for u in um.list_users():
                print(u)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

def main():
    um = UserManager()
    user = None

    while not user:
        print("=== Login ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        authenticated = um.authenticate(username, password)
        if authenticated:
            user = authenticated
        else:
            print("Invalid username or password. Please try again.")

    tm = TaskManager(current_user=user)
    # Start notification service
    user_prefs = {}  # Load or define user notification preferences here
    notifier = NotificationService(tm, um, user_prefs)
    notifier.start()

    while True:
        show_main_menu(user)
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                print("\n--- Task List ---")
                tasks = tm.list_tasks(sort_by_due_date=True)
                if tasks:
                    for t in tasks:
                        print(t)
                else:
                    print("No tasks found.")
            elif choice == "2":
                from datetime import datetime, timezone
                
                title = input("Title: ").strip()
                desc = input("Description: ").strip()
                priority = input("Priority (Low/Medium/High): ").strip() or "Medium"
                
                due_date_input = input("Due Date (YYYY-MM-DDTHH:MM:SSZ) or blank: ").strip()
                reminder_input = input("Reminder Time (YYYY-MM-DDTHH:MM:SSZ) or blank: ").strip()
                is_recurring = input("Is Recurring? (y/n): ").strip().lower() == 'y'
                recurrence_pattern = {}
                if is_recurring:
                    freq = input("Recurrence Frequency (daily/weekly/monthly): ").strip().lower()
                    interval = int(input("Recurrence Interval (number): ").strip())
                    recurrence_pattern = {'frequency': freq, 'interval': interval}
                new_task = Task(
                    title=title,
                    description=desc,
                    priority=priority,
                    due_date=due_date_input if due_date_input else None,
                    reminder_time=reminder_input if reminder_input else None,
                    is_recurring=is_recurring,
                    recurrence_pattern=recurrence_pattern
                )
                tm.add_task(new_task)
                print("Task added successfully.")
            elif choice == "3":
                title = input("Enter task title to update status: ").strip()
                new_status = input("New Status (Pending/In-Progress/Done): ").strip()
                print(update_status(tm, title, new_status, user_can_edit=True))
            elif choice == "4":
                task_id = input("Enter task ID to delete: ").strip()
                print(tm.delete_task(task_id))
            elif choice == "5":
                query = input("Enter search keyword: ").strip()
                results = search_by_title(tm, query)
                print("\n--- Search Results ---")
                for t in results:
                    print(vars(t))
            elif choice == "6":
                um.logout()
                notifier.stop()
                main()  # restart login
                return
            elif choice == "7" and user.role == "Admin":
                handle_admin_user_management(um, user.username)
            elif choice == "0":
                um.logout()
                notifier.stop()
                print("Logged out. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
