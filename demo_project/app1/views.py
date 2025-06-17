from django.shortcuts import render    #render used to create webpage responses

# (request,template_name,context)
# context : used to pass data from views to template file. it is dictionary type,variable containing keys and values


from django.http import HttpResponse

# Home view
def home(request):

     # return HttpResponse('Welcome to Home')
     context ={'name':'Ram','age':24}
     return render(request,'home.html',context)

# first view
def first_view(request):
    # return HttpResponse('First page')
    return render(request, 'first.html')
# second view
def second_view(request):
    # return HttpResponse('Second page')
    return render(request, 'second.html')
