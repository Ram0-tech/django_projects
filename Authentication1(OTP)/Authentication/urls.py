"""
URL configuration for Authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index.as_view(),name='home'),
    path('signup',views.Signup.as_view(),name='signup'),
    path('sigin',views.Login.as_view(),name='signin'),
    path('signout',views.Logout.as_view(),name='signout'),
    path('verify',views.Otpverification.as_view(),name='verify'),
    path('admin',views.AdminHome.as_view(),name='adminhome'),
    path('student',views.StudentHome.as_view(),name='student'),
    path('teacher',views.TeacherHome.as_view(),name='teacher'),
    path('accounts/',include('django.contrib.auth.urls')),
]
