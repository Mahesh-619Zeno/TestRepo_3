from users.user import UserManager
from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority

def main():
    user_manager = UserManager()
    task_manager = TaskManager()

    print("=== Multi-User Task Manager with Prioritization and Categorization ===")

    # Initialize default users and tasks if none exist
    if not user_manager.users:
        admin = user_manager.add_user("admin", "Admin")
        alice = user_manager.add_user("alice")
        bob = user_manager.add_user("bob")

        task_manager.add_task(Task("Finish Report", "Complete the financial report", "High", "Work", owner_id=admin.user_id))
        task_manager.add_task(Task("Email Client", "Send project updates", "Medium", "Communication", owner_id=alice.user_id))
        task_manager.add_task(Task("Team Meeting", "Discuss project roadmap", "Low", "Meeting", owner_id=bob.user_id))

    username = input("Enter your username: ")
    current_user = user_manager.get_user_by_username(username)

    if not current_user:
        print("User not found. Exiting.")
        return

    print(f"Welcome, {current_user.username} (Role: {current_user.role})")

    is_admin = current_user.role.lower() == "admin"

    tasks = task_manager.list_tasks(user_id=current_user.user_id, admin=is_admin)

    print("\nYour Tasks:")
    for t in tasks:
        owner_user = user_manager.get_user_by_id(t["OwnerID"])
        owner_name = owner_user.username if owner_user else "Unknown"
        shared_count = len(t["SharedWith"])
        print(f"- {t['Title']} (Owner: {owner_name}) | Priority: {t['Priority']} | Category: {t['Category']} | Status: {t['Status']} | Shared with {shared_count} users")

    # Admin panel: list all users
    if is_admin:
        print("\nRegistered Users:")
        for u_id, uname, role in user_manager.list_users():
            print(f"- {uname} (ID: {u_id}, Role: {role})")

    # Allow user to share a task they own
    if not is_admin:
        share = input("Do you want to share a task? (y/n): ").strip().lower()
        if share == "y":
            task_title = input("Enter task title to share: ")
            share_with_username = input("Enter username to share with: ")
            share_with_user = user_manager.get_user_by_username(share_with_username)
            if share_with_user:
                result = task_manager.share_task(task_title, current_user.user_id, share_with_user.user_id)
                print(result)
            else:
                print(f"User '{share_with_username}' not found.")

    # Use updated search modules considering user permissions
    print("\nSearch tasks by title:")
    search_query = input("Enter title keyword: ").strip()
    results = search_by_title(task_manager, search_query, user_id=current_user.user_id, admin=is_admin)
    for t in results:
        print(t)

    print("\nSearch tasks by priority:")
    priority_query = input("Enter priority (High/Medium/Low): ").strip()
    prio_results = search_by_priority(task_manager, priority_query, user_id=current_user.user_id, admin=is_admin)
    for t in prio_results:
        print(t)

    # Update status demo
    task_to_update = input("\nEnter task title to update status: ").strip()
    new_status = input("Enter new status: ").strip()
    update_result = update_status(task_manager, task_to_update, new_status, user_id=current_user.user_id, admin=is_admin)
    print(update_result)

if __name__ == "__main__":
    main()
