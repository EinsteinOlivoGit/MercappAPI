from django.db import models
from django.contrib.auth.models import User

class Market(models.Model):
    name = models.CharField(max_length=80)
    slogan = models.CharField(max_length=200)
    create_date = models.DateField()
    last_update_date = models.DateField()
    users = models.ManyToManyField(User)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.name
    