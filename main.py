from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority
from tasks.recurring_task import RecurringTaskManager, RecurringTaskTemplate
import uuid
from datetime import datetime

FREQUENCY_CHOICES = ['Daily', 'Weekly', 'Monthly']

def input_frequency():
    while True:
        freq = input("Enter frequency (Daily, Weekly, Monthly): ")
        if freq in FREQUENCY_CHOICES:
            return freq
        print("Invalid frequency. Please choose from Daily, Weekly, Monthly.")

def input_end_date():
    while True:
        date_str = input("Enter optional recurrence end date (YYYY-MM-DD) or leave blank: ")
        if not date_str:
            return None
        try:
            d = datetime.strptime(date_str, "%Y-%m-%d")
            if d.date() <= datetime.utcnow().date():
                print("End date must be in the future.")
                continue
            return date_str
        except ValueError:
            print("Invalid date format.")

def list_recurring(recurring_manager):
    templates = recurring_manager.list_templates()
    if not templates:
        print("No recurring task templates found.")
        return
    for t in templates:
        print(f"ID: {t['template_id']}")
        print(f"Title: {t['base_task_info']['title']}")
        print(f"Frequency: {t['frequency']}")
        print(f"Recurrence End Date: {t['recurrence_end_date']}")
        print(f"Active: {t['active']}")
        print("-----")

def edit_recurring(recurring_manager, template_id):
    t = recurring_manager.find_template(template_id)
    if not t:
        print(f"Template {template_id} not found.")
        return

    print(f"Editing template '{t.base_task_info['title']}'")

    new_title = input(f"New Title (blank to keep '{t.base_task_info['title']}'): ")
    new_frequency = input_frequency()
    new_end_date = input_end_date()

    base_task_info = t.base_task_info
    if new_title:
        base_task_info['title'] = new_title

    recurring_manager.edit_template(
        template_id,
        base_task_info=base_task_info,
        frequency=new_frequency,
        recurrence_end_date=new_end_date
    )
    print("Template updated successfully.")

def delete_recurring(recurring_manager, template_id):
    t = recurring
