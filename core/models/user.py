from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    cellphone = PhoneNumberField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code_number = models.CharField(
        max_length=4, blank=False, null=False, unique=True, validators=[MinLengthValidator(4), MaxLengthValidator[4]])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Users"