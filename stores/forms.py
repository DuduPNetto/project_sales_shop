from django import forms
from stores import models


class AddEmployeeForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        min_length=2,
        max_length=100,
        help_text='Required.',
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    birthday = forms.DateField(
        required=True
    )
    function = forms.CharField(
        required=True,
        min_length=2,
        max_length=50,
        help_text='Required.'
    )

    class Meta:
        model = models.Employee
        fields = ("name", "birthday", "function", "store",)
