from rest_framework import serializers
from habits.models import Habit
#from habits.validators import


class HabitSerializer(serializers.ModelSerializer):
    #link = serializers.CharField(validators=[wrong_links_validator])

    class Meta:
        model = Habit
        fields = "__all__"
