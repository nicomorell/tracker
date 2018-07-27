from django import forms

from .models import BMI

from django.core.validators import MaxValueValidator, MinValueValidator

class BMIForm(forms.ModelForm):
  #  weight = forms.FloatField(
     #   validators=[MinValueValidator(0.9), MaxValueValidator(58)],

 #   todays_date= forms.IntegerField(label="What is today's date?", widget=forms.Select(choices=weight)),
    class Meta:
        model = BMI
        fields = ('age', 'height', 'weight')