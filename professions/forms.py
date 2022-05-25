from django import forms
from django.contrib.auth.forms import UserCreationForm
from professions.models import User, Direction, Profile, UserDirect, UserProf





class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password',)
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password': 'Пароль',
        }


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль',
        }