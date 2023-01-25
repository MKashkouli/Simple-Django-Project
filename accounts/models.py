from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    id_code = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return f'{self.username}'

