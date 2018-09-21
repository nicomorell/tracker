from django import forms
from .models import BMI, Weight

class BMIForm(forms.ModelForm):

    class Meta:
        model = BMI
        fields = ('age', 'heightFeet', 'heightMetres', 'heightInches', 'weightPounds', 'weightKilos')

class weightForm(forms.ModelForm):
    prevWeight = forms.FloatField(required = False)
    afterWeight = forms.FloatField(required=False)
    prevDay = forms.IntegerField(required = False)
    afterDay = forms.IntegerField(required=False)
    class Meta:
        model = Weight
        fields = ('mass', 'day', 'month', 'year')