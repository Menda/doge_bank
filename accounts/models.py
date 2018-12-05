from django.conf import settings
from django.db import models
from localflavor.generic.models import IBANField


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    iban = IBANField(help_text='International Bank Account Number')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
