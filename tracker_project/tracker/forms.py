from django import forms

from .models import BMI

class BMIForm(forms.ModelForm):

    class Meta:
        model = BMI
        fields = ('age', 'heightFeet', 'heightInches', 'weightPounds')