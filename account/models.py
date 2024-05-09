from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=50)
    POINT_CHOICES = (
        (0, 'None'),
        (1, 'Bronze'),
        (2, 'Silver'),
        (3, 'Gold'),
    )
    point = models.IntegerField(choices=POINT_CHOICES, default=0)
    