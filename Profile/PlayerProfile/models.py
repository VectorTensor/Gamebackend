from django.db import models

# Create your models here.

class Profile(models.Model):

    id_hash = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name








