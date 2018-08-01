from django.db import models


class BMI(models.Model):
    age = models.PositiveIntegerField()
    heightFeet = models.FloatField()
    heightInches = models.FloatField()
    weightPounds = models.FloatField()
