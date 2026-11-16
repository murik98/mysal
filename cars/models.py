from django.db import models

class Cars(models.Model):
    model = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    cost = models.IntegerField(max_length=50)