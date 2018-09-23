from django import forms
from .models import BMI, Weight
from django.contrib.auth.models import User
from tracker.models import UserProfile


class BMIForm(forms.ModelForm):
    class Meta:
        model = BMI
        fields = ('age', 'heightFeet', 'heightMetres', 'heightInches', 'weightPounds', 'weightKilos')

class weightForm(forms.ModelForm):
    prevWeight = forms.FloatField(required = False, label = 'prevWeight')
    afterWeight = forms.FloatField(required=False)
    prevDay = forms.IntegerField(required = False)
    afterDay = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(weightForm, self).__init__(*args, **kwargs)
        self.fields['prevWeight'].widget.attrs.update({'class': 'myfieldclass'})

    class Meta:
        model = Weight
        fields = ('mass', 'day', 'month', 'year')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None,
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')