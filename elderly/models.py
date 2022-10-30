from django.db import models
from django.contrib.auth.models import User


class Elderly(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=300)

    def __str__(self):
        return str(self.user)

