from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class formWinners(forms.Form):
    client_id = forms.CharField(max_length=30)
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    draw = forms.CharField(max_length=30)
    prize = forms.CharField(max_length=30)