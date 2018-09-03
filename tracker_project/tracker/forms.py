from django import forms
from .models import BMI, Weight

class BMIForm(forms.ModelForm):

    class Meta:
        model = BMI
        fields = ('age', 'heightFeet', 'heightMetres', 'heightInches', 'weightPounds', 'weightKilos')

class weightForm(forms.ModelForm):
    changeWeight = forms.FloatField(label='Weight')
    changeDay = forms.IntegerField(label='Day')
    class Meta:
        model = Weight
        fields = ('mass', 'day', 'month', 'year')