from django.db import models

class Company(models.Model):
    company_email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}"

# Create your models here.
