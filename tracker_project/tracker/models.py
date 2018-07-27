from django.db import models


class BMI(models.Model):
    age = models.PositiveIntegerField()
    height = models.FloatField()
    weight = models.FloatField()