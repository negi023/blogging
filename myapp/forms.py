from django import forms
from django.contrib.auth.models import User  # built-in user model
from django.contrib.auth.forms import UserCreationForm  # in-built form
from .models import Profile


class Registrationform(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:  # information about the model
        model = User  # this model is referring to User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)  # listing the names of the fields you want to use


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dp']
