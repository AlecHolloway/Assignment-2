from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0, blank=True, null=True)
    income = models.IntegerField(default=0, blank=True, null=True)
    years = models.IntegerField(default=0, blank=True, null=True)
    weight = models.IntegerField(default=0, blank=True, null=True)
    feet = models.IntegerField(default=0, blank=True, null=True)
    inches = models.IntegerField(default=0, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
