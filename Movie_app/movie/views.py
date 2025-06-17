from django.shortcuts import render,redirect
from movie.forms import MovieForm
from movie.models import Movie
def movie_list(request):
    m=Movie.objects.all()
    return render(request,'movie.html',{'movie':m})

def add(request):
    if request.method=='POST':
       form_instance=MovieForm(request.POST,request.FILES)
       if form_instance.is_valid():
           form_instance.save()

       return redirect('movie_list')
    form_instance=MovieForm()
    return render(request,'add.html',{'forms':form_instance})

def details(request,i):
    m=Movie.objects.get(id=i)

    return render(request, 'details.html',{'movie':m})

def edit(request,i):
    m = Movie.objects.get(id=i)
    if request.method == 'POST':
        form_instance = MovieForm(request.POST, request.FILES,instance=m)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('movie_list')
    form_instance = MovieForm(instance=m)
    return render(request, 'edit.html', {'forms': form_instance})

def delete(request,i):
    Movie.objects.get(id=i).delete()
    return redirect('movie_list')