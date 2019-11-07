from django import forms
from phonenumber_field.formfields import PhoneNumberField

class UserForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    cellphone = PhoneNumberField(required=True)