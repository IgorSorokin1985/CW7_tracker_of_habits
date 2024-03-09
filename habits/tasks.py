from habits.utils import send_telegram_message
from celery import shared_task
from habits.models import Habit
from datetime import datetime


@shared_task
def check_habits_for_action():
    habits = Habit.objects.all()
    now = datetime.now().time()
    for habit in habits:
        if not habit.next_date:
            print(habit.time)
            print(now)
            if habit.time < now:
                send_telegram_message(habit)
