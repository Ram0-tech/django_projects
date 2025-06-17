from django.shortcuts import render

def bmi(request):
    if(request.method=='POST'):
        weight=float(request.POST['w'])
        height=float(request.POST['h'])/100
        bmi = weight / (height ** 2)
        context={'result':bmi}
        return render(request,'bmi.html',context)
    return render(request,'bmi.html')
