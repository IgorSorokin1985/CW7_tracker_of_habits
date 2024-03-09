from rest_framework import serializers
from datetime import timedelta, time, datetime


def check_duration_time(duration):
    duration_seconds = duration.hour * 3600 + duration.minute * 60 + duration.second
    if duration_seconds >= 120:
        raise serializers.ValidationError("Time for habit should be mo more 120 seconds")


def check_habit_periodicity(days):
    if days > 7:
        raise serializers.ValidationError("Periodicity for habit should be mo more 7 days")


def validate_fields(reward, associated_nice_habit):
    if reward and associated_nice_habit:
        raise serializers.ValidationError("Habit can have reward OR associated nice habit")
    if not reward and not associated_nice_habit:
        raise serializers.ValidationError("Habit should have reward or associated nice habit")
