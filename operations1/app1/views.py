from django.shortcuts import render
from app1.forms import *


def addition(request):
    if request.method == 'POST':
        print(request.POST)
        return render(request, 'add.html')

    form_instance = AdditionForm()
    return render(request, 'add.html', {'form': form_instance})

def factorial(request):
    if request.method == 'POST':
        print(request.POST)
        return render(request, 'factorial.html')
    form_instance = FactForm()
    return render(request,'factorial.html',{'forms':form_instance})

def bmi(request):
    if(request.method=='POST'):
        print(request.POST)
        return render(request,'bmi.html',)
    form_instance=BmiForm()
    return render(request,'bmi.html',{'form':form_instance})


def signup(request):
    if(request.method=='POST'):
        return render(request,'signup.html')
    form_instance=SignupForm()
    return render(request,'signup.html',{'form':form_instance})

def calorie(request):
    if (request.method == 'POST'): #after form submission
        print(request.POST)
        form_instance=CalorieForm(request.POST) #creating form object using data submitted by user
        if form_instance.is_valid(): #checking the validity of data using is_valid()
           data=form_instance.cleaned_data
           gender=data['gender']
           weight=data['Weight']
           height=data['Height']
           age=data['Age']
           activity_level=data['activityLevel']
           print(weight,height,gender,age,activity_level)
           if gender=='Male':
               bmr=10 * weight + 6.25 * height - 5 * age + 5
           else:
            bmr=10 * weight+ 6.25 * height- 5 * age - 161
           c=bmr*float(activity_level)
           print(c)#accessing the cleaned data after validation
        return render(request, 'calorie.html',{'form':form_instance,'result':c})
    if request.method=='GET':

     form_instance = CalorieForm()
     return render(request, 'calorie.html', {'form': form_instance})