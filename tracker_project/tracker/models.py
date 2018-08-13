from django.db import models


class BMI(models.Model):
    age = models.PositiveIntegerField(blank = False)
    heightFeet = models.FloatField(blank = False)
    heightInches = models.FloatField(blank = True, null=True)
    heightMetres = models.PositiveIntegerField(blank = True, null=False)
    weightPounds = models.FloatField(blank = True, null=True)
    weightKilos = models.FloatField(blank = True, null=True)






