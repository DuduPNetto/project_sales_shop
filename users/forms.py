from django import forms
from django.contrib.auth.models import User


class AddUserForm(forms.ModelForm):
    username = forms.CharField(required=True, min_length=4, max_length=50)
    first_name = forms.CharField(required=True, min_length=3, max_length=50)
    last_name = forms.CharField(required=True, min_length=3, max_length=100)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password")
