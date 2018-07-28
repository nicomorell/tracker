from django import forms

from .models import BMI

from django.core.validators import MaxValueValidator, MinValueValidator

class BMIForm(forms.ModelForm):

    SYSTEM = [('Metric', 'cm'),
               ('Imperial', 'ft')]

    like = forms.ChoiceField(choices=SYSTEM, widget=forms.RadioSelect())
    class Meta:
        model = BMI

        fields = ('age', 'height', 'weight')