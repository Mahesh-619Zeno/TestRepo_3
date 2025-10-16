import json
import os
import uuid
from datetime import datetime, timedelta

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/recurring_tasks_data.json")


class RecurringTaskTemplate:
    ALLOWED_FREQUENCIES = ['Daily', 'Weekly', 'Monthly']

    def __init__(self, template_id, base_task_info, frequency, recurrence_end_date=None, last_generated_at=None, active=True):
        self.template_id = template_id
        self.base_task_info = base_task_info
        self.frequency = frequency
        self.recurrence_end_date = recurrence_end_date  # ISO string e.g. '2025-12-31'
        self.last_generated_at = last_generated_at or datetime.utcnow().isoformat()
        self.active = active

    def to_dict(self):
        return {
            "template_id": self.template_id,
            "base_task_info": self.base_task_info,
            "frequency": self.frequency,
            "recurrence_end_date": self.recurrence_end_date,
            "last_generated_at": self.last_generated_at,
            "active": self.active
        }

    @staticmethod
    def from_dict(data):
        return RecurringTaskTemplate(
            template_id=data['template_id'],
            base_task_info=data['base_task_info'],
            frequency=data['frequency'],
            recurrence_end_date=data.get('recurrence_end_date'),
            last_generated_at=data['last_generated_at'],
            active=data.get('active', True)
        )


class RecurringTaskManager:
    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.templates = []
        self.load_templates()

    def load_templates(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.templates = [RecurringTaskTemplate.from_dict(d) for d in data]

    def save_templates(self):
        data = [t.to_dict() for t in self.templates]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def add_template(self, template):
        if template.frequency not in RecurringTaskTemplate.ALLOWED_FREQUENCIES:
            raise ValueError(f"Invalid frequency {template.frequency}. Allowed: {RecurringTaskTemplate.ALLOWED_FREQUENCIES}")
        self.templates.append(template)
        self.save_templates()

    def list_templates(self):
        return [t.to_dict() for t in self.templates]

    def find_template(self, template_id):
        for t in self.templates:
            if t.template_id == template_id:
                return t
        return None

    def edit_template(self, template_id, **kwargs):
        t = self.find_template(template_id)
        if not t:
            return False
        if "base_task_info" in kwargs:
            t.base_task_info = kwargs["base_task_info"]
        if "frequency" in kwargs:
            if kwargs["frequency"] not in RecurringTaskTemplate.ALLOWED_FREQUENCIES:
                raise ValueError(f"Invalid frequency {kwargs['frequency']}")
            t.frequency = kwargs["frequency"]
        if "recurrence_end_date" in kwargs:
            t.recurrence_end_date = kwargs["recurrence_end_date"]
        if "active" in kwargs:
            t.active = kwargs["active"]
        self.save_templates()
        return True

    def delete_template(self, template_id):
        self.templates = [t for t in self.templates if t.template_id != template_id]
        self.save_templates()

    def _get_next_date(self, last_date, frequency):
        last = datetime.fromisoformat(last_date)
        if frequency == 'Daily':
            return last + timedelta(days=1)
        elif frequency == 'Weekly':
            return last + timedelta(weeks=1)
        elif frequency == 'Monthly':
            # Approximate 1 month as 30 days
            return last + timedelta(days=30)
        else:
            raise ValueError("Unknown frequency")

    def generate_tasks(self):
        now = datetime.utcnow()
        created_tasks = []
        for template in self.templates:
            if not template.active:
                continue
            last_generated = datetime.fromisoformat(template.last_generated_at)
            next_date = self._get_next_date(template.last_generated_at, template.frequency)
            end_date = datetime.fromisoformat(template.recurrence_end_date) if template.recurrence_end_date else None

            if next_date <= now and (end_date is None or next_date <= end_date):
                base = template.base_task_info
                new_task = self.task_manager.Task(
                    title=base['title'],
                    description=base.get('description', ''),
                    priority=base.get('priority', 'Medium')
                )
                self.task_manager.add_task(new_task)
                template.last_generated_at = next_date.isoformat()
                created_tasks.append(new_task)
        self.save_templates()
        return created_tasks
