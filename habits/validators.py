from rest_framework import serializers
from habits.models import Habit


def check_time_for_habit(time):
    if time > 120:
        raise serializers.ValidationError("Time for habit should be mo more 120 seconds")


def check_habit_periodicity(days):
    if days > 7:
        raise serializers.ValidationError("Periodicity for habit should be mo more 7 days")


def validate_fields(is_nice_habit, reward, associated_habit):
    if is_nice_habit:
        if reward or associated_habit:
            raise serializers.ValidationError("Nice habit cannot have reward or associated habit")
    else:
        if reward and associated_habit:
            raise serializers.ValidationError("Habit can have reward OR associated nice habit")
        if associated_habit:
            if not associated_habit.is_nice_habit:
                raise serializers.ValidationError("Associated habit should be NICE habit")
        if not reward and not associated_habit:
            raise serializers.ValidationError("Habit should have reward or associated nice habit")

