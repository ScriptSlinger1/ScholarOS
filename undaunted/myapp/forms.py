from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomStudent


class CustomStudentForm(UserCreationForm):
    class Meta:
        model = CustomStudent
        fields = ['username', 'email', 'first_name', 'last_name', 'bio']