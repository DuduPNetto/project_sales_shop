from typing import Any, Dict
from django import forms
from stores import models


class AddProductForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        max_length=255,
        help_text='Required.',
        error_messages={
            'max_length': 'Please, add less than 255 letters.'
        }
    )
    price = forms.FloatField(required=True, min_value=0, help_text='Required.',)
    stock = forms.IntegerField(
        min_value=0, required=True, help_text='Required.',)
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )

    class Meta:
        model = models.StoreProduct
        fields = ("name", "short_description",
                  "long_description", "price", "stock", "store", "image")


class AddEmployeeForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        min_length=3,
        max_length=100,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    age = forms.IntegerField(
        min_value=16,
        max_value=100,
        required=True,
        help_text='Required.',
        error_messages={
            'min_value': 'Min Age 16 years.',
            'max_value': 'Max Age 100 years.'
        }
    )
    function = forms.CharField(
        required=True,
        min_length=2,
        max_length=50,
        help_text='Required.'
    )

    class Meta:
        model = models.Employee
        fields = ("name", "age", "function", "email", "store",)
