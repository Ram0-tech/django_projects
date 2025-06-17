from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def add_books(request):
    return render(request,'add_books.html')
def view_book(request):
    return render(request,'view_book.html')