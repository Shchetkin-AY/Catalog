from django import forms
from django.contrib.auth.forms import UserCreationForm
from professions.models import User, UserDirect, UserProf


# форма направлений пользователя
class UserDirectionForm(forms.ModelForm):
    class Meta:
        model = UserDirect
        fields = ('__all__')


# форма профилей пользователя
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProf
        fields = ('__all__')


# форма Создани пользователя
class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)


# форма аутентификации
class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
