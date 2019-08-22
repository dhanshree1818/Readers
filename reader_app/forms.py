from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import DateInput

from .models import Register


class RegisterForm(UserCreationForm):

    class Meta:
        model = Register
        fields = ["first_name", "last_name", "username", "dob", "password1", "password2", "recovery_email", "Agree_Toc"]
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }
