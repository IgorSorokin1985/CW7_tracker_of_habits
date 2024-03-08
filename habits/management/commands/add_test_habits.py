from django.core.management import BaseCommand
from habits.models import Habit

test_habits = [
    {
        "id": 1,
        "user_id": 1,
        "place": "home",
        "action": "eat desert",
        "is_nice_habit": True,
        "periodicity": 1,
        "is_public": False,
        "time_for_habit": 120,
    },
    {
        "id": 2,
        "user_id": 1,
        "place": "home",
        "action": "drink water",
        "is_nice_habit": False,
        "reward": "10 DKK",
        "periodicity": 1,
        "is_public": False,
        "time_for_habit": 15,
    },
    {
        "id": 3,
        "user_id": 1,
        "place": "home",
        "action": "not drink alcohol",
        "is_nice_habit": False,
        "reward": "15 DKK",
        "periodicity": 1,
        "is_public": False,
        "time_for_habit": 15,
    },
    {
        "id": 4,
        "user_id": 1,
        "place": "home",
        "action": "clean restroom",
        "is_nice_habit": False,
        "associated_habit_id": 1,
        "periodicity": 3,
        "is_public": False,
        "time_for_habit": 120,
    },
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        Habit.objects.all().delete()
        print('Old habits were deleted')
        for test_habit in test_habits:
            new_habit = Habit.objects.create(**test_habit)
            new_habit.save()
        print('Test habits were added in database')
