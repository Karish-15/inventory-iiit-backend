from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    contact = models.CharField(max_length=20, blank=True, null=True)
    misc_details = models.TextField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)


