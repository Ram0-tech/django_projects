from django.shortcuts import render,redirect
from app1.models import Employee
from app1.forms import EmpForm
def emp_list(request):
    e=Employee.objects.all()
    return render(request,'emp_list.html',{'emp':e})


def add(request):
    if request.method=='POST':
        print('hello')
        form_instance=EmpForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('emp_list')
    form_instance=EmpForm()
    return render(request,'add.html',{'forms':form_instance})
def details(request,i):
    e=Employee.objects.get(id=i)
    return render(request,'details.html',{'emp':e})
def delete(request,i):
     Employee.objects.get(id=i).delete()
     return redirect('emp_list')


def edit(request,i):
    e = Employee.objects.get(id=i)
    if request.method=='POST':
        form_instance=EmpForm(request.POST,request.FILES,instance=e)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('emp_list')
    form_instance=EmpForm(instance=e)
    return render(request,'edit.html',{'forms':form_instance})