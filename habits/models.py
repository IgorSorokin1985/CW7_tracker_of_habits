from django.db import models
from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='user')
    place = models.CharField(max_length=50, verbose_name='Place')
    action = models.CharField(max_length=50, verbose_name='Action')
    is_nice_habit = models.BooleanField(verbose_name='Is nice habit?')
    reward = models.CharField(max_length=50, **NULLABLE, verbose_name='Reward')
    associated_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Associated habit')
    periodicity = models.PositiveIntegerField(verbose_name='Periodicity')
    is_public = models.BooleanField(default=False, verbose_name='Is public')
    time_for_habit = models.PositiveIntegerField(verbose_name='Time for habit')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'
