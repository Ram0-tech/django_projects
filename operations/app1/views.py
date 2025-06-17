from django.shortcuts import render

def addition(request):
    if(request.method=='POST'):
        print(request.POST)
        n1=request.POST['num1']
        n2=request.POST['num2']
        result=int(n1)+int(n2)
        # print(result)
        context={'result':result}
        return render(request,'add.html',context)

    return render(request,'add.html')

def factorial(request):
    if (request.method == 'POST'):

        n=int(request.POST['n1'])
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        context = {'result': fact}
        return render(request, 'factorial.html', context)
    return render(request,'factorial.html')

def bmi(request):
    if(request.method=='POST'):
        weight=float(request.POST['w'])
        height=float(request.POST['h'])/100
        bmi = weight / (height ** 2)
        context={'result':bmi}
        return render(request,'bmi.html',context)
    return render(request,'bmi.html')
