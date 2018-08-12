from django import forms

from .models import BMI

class BMIFormImperial(forms.ModelForm):

    class Meta:
        model = BMI
        fields = ('age', 'heightFeet', 'heightInches', 'weightPounds')

class BMIFormMetric(forms.ModelForm):

    class Meta:
        model = BMI
        fields = ('age', 'heightMetres', 'weightKilos')