from django.db import models
from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class NiceHabit(models.Model):
    """Model for Nice Habit"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    place = models.CharField(max_length=50, **NULLABLE, verbose_name='Place')
    action = models.CharField(max_length=50, verbose_name='Action')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Nice habit'
        verbose_name_plural = 'Nice habits'


class Habit(models.Model):
    """Model for Habit"""
    user = models.ForeignKey(User, **NULLABLE, on_delete=models.CASCADE, verbose_name='user')
    time = models.TimeField(verbose_name='Time for habit')
    place = models.CharField(max_length=50, verbose_name='Place')
    action = models.CharField(max_length=50, verbose_name='Action')
    reward = models.CharField(max_length=50, **NULLABLE, verbose_name='Reward')
    associated_nice_habit = models.ForeignKey(NiceHabit, on_delete=models.SET_NULL,
                                              **NULLABLE, verbose_name='Associated nice habit')
    periodicity = models.PositiveIntegerField(verbose_name='Periodicity')
    is_public = models.BooleanField(default=False, verbose_name='Is public')
    duration_time = models.TimeField(verbose_name='Duration time')
    next_date = models.DateField(**NULLABLE, verbose_name="Date for next action of habit")

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'
