from django.db import models

# Create your models here.
class Patent(models.Model):
    patent_data=models.TextField()
    patent_date=models.DateField()