from django import forms
from django.forms import PasswordInput


class AdditionForm(forms.Form):
    Number1 = forms.IntegerField()
    Number2 = forms.IntegerField()


class FactForm(forms.Form):
    Number = forms.IntegerField()


class BmiForm(forms.Form):
    Weight = forms.FloatField()
    Height = forms.FloatField()

class SignupForm(forms.Form):
    username=forms.CharField()
    Password=forms.CharField(widget=PasswordInput)
    Email=forms.EmailField()
    gender_choices=[('male','Male'),('female','Female',),('others','Others')]
    gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)

    role_choices=[('admin','Admin'),('student','Student')]
    roles=forms.ChoiceField(choices=role_choices)

class CalorieForm(forms.Form):
    gender_choices = [('male', 'Male'), ('female', 'Female',), ('others', 'Others')]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    # Weight = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    Weight = forms.FloatField()
    Height = forms.FloatField()
    Age=forms.IntegerField()
    activity_level_choices = [('1.2', 'Sedentary(little/no exercise)'), ('1.375', '  Lightly active (light exercise/sports 1-3 days/week) '),('1.55',' Moderately active (moderate exercise/sports 3-5 days/week)'),('1.725','Very active (hard exercise/sports 6-7 days a week)'),('1.9',' Extra active (very hard exercise/sports & physical job or 2x training)')]
    activityLevel = forms.ChoiceField(choices=activity_level_choices)