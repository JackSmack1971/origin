from django.db import models
from django.contrib.auth.models import User

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

User.add_to_class('mfa_enabled', models.BooleanField(default=False))