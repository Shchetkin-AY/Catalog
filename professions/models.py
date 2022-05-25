from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Direction(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


class Profile(models.Model):
    name = models.CharField(max_length=100)
    direct = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='direct')

    def __str__(self):
        return f"{self.name}"


class UserDirect(models.Model):
    position = models.IntegerField(auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direct = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='user_direct')

class UserProf(models.Model):
    position = models.IntegerField(auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_prof')