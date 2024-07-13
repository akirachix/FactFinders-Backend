from django.db import models
from company.models import Company


class Donation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_email = models.EmailField(primary_key=True)
    item_description = models.CharField(max_length=100)
    item_quantity = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)
    pickup_date=models.DateTimeField()

    def __str__(self):
        return f"{self.item_description}"

# Create your models here.
