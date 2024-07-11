from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_hash = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name








