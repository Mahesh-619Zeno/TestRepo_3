from task.task import Task, TaskManager
from task.status import update_status
from task.search import search_by_title
from task.auth import AuthSystem

def main():
    auth = AuthSystem()
    current_user = auth.login()
    manager = TaskManager(current_user)

    while True:
        print("\n=== Task Manager CLI ===")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Update Status")
        print("4. Share Task")
        print("5. Manage Users (Admin Only)")
        print("6. Switch User")
        print("7. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            for t in manager.list_tasks():
                print(t)

        elif choice == "2":
            title = input("Task Title: ")
            desc = input("Description: ")
            pri = input("Priority (High/Medium/Low): ")
            print(manager.add_task(Task(title, desc, pri, manager.current_user.user_id)))

        elif choice == "3":
            title = input("Task Title to update: ")
            status = input("New Status: ")
            print(update_status(manager, title, status))

        elif choice == "4":
            task_id = input("Task ID: ")
            username = input("Share with username: ")
            from task.users import UserManager
            um = UserManager()
            user = um.find_by_username(username)
            if user:
                print(manager.share_task(task_id, user.user_id))
            else:
                print("User not found.")

        elif choice == "5":
            if current_user.role != "Admin":
                print("Admin access required.")
                continue
            from task.users import UserManager
            um = UserManager()
            print("\n--- User Management ---")
            print("a. Add User")
            print("b. Remove User")
            print("c. List Users")
            action = input("Select action: ")
            if action == "a":
                uname = input("Username: ")
                pwd = input("Password: ")
                role = input("Role (Admin/User): ")
                print(um.add_user(uname, pwd, role))
            elif action == "b":
                uname = input("Username to remove: ")
                print(um.remove_user(uname, current_user))
            elif action == "c":
                for u in um.list_users():
                    print(u)

        elif choice == "6":
            current_user = auth.switch_user()
            manager = TaskManager(current_user)

        elif choice == "7":
            auth.logout()
            break

if __name__ == "__main__":
    main()
