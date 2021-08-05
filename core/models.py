from django.db import models

class PeronalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    best_food = models.CharField(max_length=100)
    age = models.IntegerField()
    