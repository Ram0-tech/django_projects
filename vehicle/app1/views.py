from urllib import request

from django.shortcuts import render,redirect
from app1.models import Vehicle
from app1.forms import VForm
def vehiclelist(request):
    v=Vehicle.objects.all()
    return render(request,'vehiclelist.html',{'vehicle':v})

def add(request):
    if request.method=='POST':
        form_instance=VForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('vehiclelist')
    form_instance=VForm()
    return render(request,'add.html',{'forms':form_instance})


