from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Model for users"""
    username = None
    name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(unique=True, verbose_name='Email')
    telegram = models.CharField(max_length=50, verbose_name='Telegram')
    avatar = models.ImageField(upload_to='users', **NULLABLE, verbose_name='Avatar')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
