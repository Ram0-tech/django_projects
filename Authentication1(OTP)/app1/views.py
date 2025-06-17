from django.shortcuts import render,redirect

from django.views import View
from app1.forms import SignupForm
from app1.forms import LoginForm
from django.contrib.auth import authenticate,login,logout

class Index(View):
    def get(self,request):
        return render(request,'home.html')

from django.core.mail import send_mail
class Signup(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            user=form_instance.save(commit=False)
            user.is_active=False
            user.save()
            user.generate_otp()
            send_mail(
                "Django Auth OTP",
                user.otp,
                "ramprakashkp048@gmail.com",
                [user.email],
                fail_silently=False,
            )
            return redirect('verify')
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
            if user and user.is_superuser==True:
                login(request,user)
                return redirect('adminhome')
                #starting session using current user
            elif user and user.role=='student':
                login(request, user)
                return redirect('student')
            elif user and user.role == 'teacher':
                login(request, user)
                return redirect('teacher')
            else:
                print('Invalid User Credentials...')
                return redirect('signin')

    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})

class Logout(View):
    def get(self,request):
      logout(request)
      return redirect('signin')
from app1.models import User
from django.contrib import messages
class Otpverification(View):
    def post(self,request):
        o=request.POST['otp']
        try:
            u=User.objects.get(otp=o)
            u.is_active=True
            u.is_verified=True
            u.otp=None
            u.save()
            return redirect('login')
        except:
          # print('Invalid OTP')
          messages.error(request,'Invalid OTP')
          return redirect('verify')
    def get(self,request):
        return render(request,'otp_verification.html')


class AdminHome(View):
    def get(self,request):
        return render(request,'admin.html')

class StudentHome(View):
    def get(self,request):
        return render(request,'student.html')

class TeacherHome(View):
    def get(self,request):
        return render(request,'teacher.html')

