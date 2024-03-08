from rest_framework import serializers
from habits.models import Habit
from habits.validators import check_time_for_habit, check_habit_periodicity, validate_fields


class HabitSerializer(serializers.ModelSerializer):
    time_for_habit = serializers.IntegerField(validators=[check_time_for_habit])
    periodicity = serializers.IntegerField(validators=[check_habit_periodicity])

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        if data.get('is_nice_habit'):
            is_nice_habit = data.get('is_nice_habit')
        else:
            is_nice_habit = None
        if data.get('reward'):
            reward = data.get('reward')
        else:
            reward = None
        if data.get('associated_habit'):
            associated_habit = data.get('associated_habit')
        else:
            associated_habit = None
        validate_fields(is_nice_habit, reward, associated_habit)
        return data


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["action", "is_nice_habit", "reward", "associated_habit", "periodicity", "time_for_habit", "is_public", ]
