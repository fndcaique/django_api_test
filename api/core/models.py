from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    age = models.IntegerField()

    def __str__(self):
        return self.name
