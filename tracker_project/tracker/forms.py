from django import forms
from .models import BMI, Weight

class BMIForm(forms.ModelForm):

    class Meta:
        model = BMI
        fields = ('age', 'heightFeet', 'heightMetres', 'heightInches', 'weightPounds', 'weightKilos')

class weightForm(forms.ModelForm):
    prevWeight = forms.FloatField(required = False, label = 'prevWEight')
    afterWeight = forms.FloatField(required=False)
    prevDay = forms.IntegerField(required = False)
    afterDay = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(weightForm, self).__init__(*args, **kwargs)
        self.fields['prevWeight'].widget.attrs['placeholder'] = 'Previous Weight'
    class Meta:
        model = Weight
        fields = ('mass', 'day', 'month', 'year')