from django.db import models


class BMI(models.Model):
    age = models.PositiveIntegerField(blank = False)
    heightFeet = models.FloatField(blank = False)
    heightInches = models.FloatField(blank = False)
    weightPounds = models.FloatField(blank = False)





