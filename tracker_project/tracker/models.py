from django.contrib.auth.models import User
from django.db import models

class BMI(models.Model):
    age = models.PositiveIntegerField(blank = True, null = False)
    heightFeet = models.FloatField(blank = True, null = False)
    heightInches = models.FloatField(blank = True, null=True)
    heightMetres = models.FloatField(blank = True, null=False)
    weightPounds = models.FloatField(blank = True, null=True)
    weightKilos = models.FloatField(blank = True, null=True)
    
class Weight(models.Model):
    mass = models.FloatField(blank = False, null = True)
    day = models.PositiveIntegerField(blank = False, null=True)
    month = models.PositiveIntegerField(blank = True, null=True)
    year = models.PositiveIntegerField(blank = True, null=False)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username






