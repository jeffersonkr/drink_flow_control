from django import forms
from phonenumber_field.formfields import PhoneNumberField

class UserForm(forms.Form):
    nome = forms.CharField(label='name', max_length=100)
    cellphone = PhoneNumberField()