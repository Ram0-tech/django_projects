from django.shortcuts import render

from django.http import HttpResponse

#Home view


def home(request):
    return HttpResponse("Django")


# index view
def index(request):
    return HttpResponse('Welcome to Django')