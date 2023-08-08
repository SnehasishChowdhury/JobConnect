from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django import forms
from .models import CustomUser

class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = CustomUser
