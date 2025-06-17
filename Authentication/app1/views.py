from django.shortcuts import render,redirect

from django.views import View
from app1.forms import SignupForm
from app1.forms import LoginForm
from django.contrib.auth import authenticate,login,logout

class Index(View):
    def get(self,request):
        return render(request,'home.html')

class Signup(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            # user=form_instance.save(commit=False) #here user represents model_instance created
            # #user.set_password(raw_data)
            # user.set_password(form_instance.cleaned_data['password']) #changes the plain text password format into encrypted format using django's SHA algorithm.
            #                                                         #so here we call built-in  fn set_password
            # user.save()
             form_instance.save()
             return redirect('home')
        return render(request,'signup.html',{'form':form_instance})
    def get(self,request):
        form_instance=SignupForm
        return render(request,'signup.html',{'form':form_instance})


class Login(View):
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            # user=User.objects.get(username=name)
            # print(name,pwd)
            user=authenticate(username=name,password=pwd)
            # authenticate() returns user object if all the user credentials are correct, else none
            if user:
                #starting session using current user
                login(request,user)
                return redirect('home')
            else:
                print('Invalid User Credentials...')
                return redirect('login')

    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})

class Logout(View):
    def get(self,request):
      logout(request)
      return redirect('login')