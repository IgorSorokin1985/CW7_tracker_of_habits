from rest_framework import serializers


def check_duration_time(duration):
    """Checking duration of habit. Duration should not be more than 120 seconds"""
    duration_seconds = duration.hour * 3600 + duration.minute * 60 + duration.second
    if duration_seconds >= 120:
        raise serializers.ValidationError("Time for habit should be mo more 120 seconds")


def check_habit_periodicity(days):
    """Checking periodicity of habit. Periodicity should not be more than 7 days"""
    if days > 7:
        raise serializers.ValidationError("Periodicity for habit should be mo more 7 days")


def validate_fields(reward, associated_nice_habit):
    """Validating habit's fields. Habit should have a reward or associated nice habit. Not both fields."""
    if reward and associated_nice_habit:
        raise serializers.ValidationError("Habit can have a reward OR associated nice habit")
    if not reward and not associated_nice_habit:
        raise serializers.ValidationError("Habit should have a reward or associated nice habit")
