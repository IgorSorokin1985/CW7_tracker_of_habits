# Generated by Django 4.2.7 on 2024-03-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Time for habit')),
                ('place', models.CharField(max_length=50, verbose_name='Place')),
                ('action', models.CharField(max_length=50, verbose_name='Action')),
                ('reward', models.CharField(blank=True, max_length=50, null=True, verbose_name='Reward')),
                ('periodicity', models.PositiveIntegerField(verbose_name='Periodicity')),
                ('is_public', models.BooleanField(default=False, verbose_name='Is public')),
                ('duration_time', models.DurationField(verbose_name='Duration time')),
                ('next_date', models.DateField(blank=True, null=True, verbose_name='Date for next action of habit')),
            ],
            options={
                'verbose_name': 'Habit',
                'verbose_name_plural': 'Habits',
            },
        ),
        migrations.CreateModel(
            name='NiceHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=50, null=True, verbose_name='Place')),
                ('action', models.CharField(max_length=50, verbose_name='Action')),
            ],
            options={
                'verbose_name': 'Nice habit',
                'verbose_name_plural': 'Nice habits',
            },
        ),
    ]
