
from django.db import models

class BMI(models.Model):
    age = models.PositiveIntegerField(blank = True, null = False)
    heightFeet = models.FloatField(blank = True, null = False)
    heightInches = models.FloatField(blank = True, null=True)
    heightMetres = models.FloatField(blank = True, null=False)
    weightPounds = models.FloatField(blank = True, null=True)
    weightKilos = models.FloatField(blank = True, null=True)
    
class Weight(models.Model):
    mass = models.FloatField(blank = True, null = True)
    day = models.PositiveIntegerField(blank = True, null=True)
    month = models.PositiveIntegerField(blank = True, null=True)
    year = models.PositiveIntegerField(blank = True, null=False)






