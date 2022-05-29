from django.db import models
from django.contrib.auth.models import User


# Модель Направлений
class Direction(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"


# модель Профилей
class Profile(models.Model):
    name = models.CharField(max_length=100)
    direct = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='direct')

    def __str__(self):
        return f"{self.name}"


# модель выбранных пользователем Направлений
class UserDirect(models.Model):
    directionIndex = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direct = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='user_direct')

    class Meta:
        ordering = ['directionIndex']


# модель выбранных Профилей
class UserProf(models.Model):
    position = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profileIndex = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_prof')

    class Meta:
        ordering = ['profileIndex']
