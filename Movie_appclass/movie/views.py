from django.shortcuts import render,redirect
from movie.forms import MovieForm
from movie.models import Movie
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
class MovieList(ListView):
   model=Movie
   template_name = 'movie.html'
   context_object_name = 'movie'




class AddMovieView(CreateView):
    form_class = MovieForm
    template_name = 'add.html'
    model = Movie
    success_url = reverse_lazy('movie_list')


from django.views.generic import DetailView
class Details(DetailView):
    model = Movie
    template_name = 'details.html'
    context_object_name = 'movie'


from django.views.generic import UpdateView
class Edit(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'edit.html'
    success_url = reverse_lazy('movie_list')

from django.views.generic import DeleteView
class Delete(DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url = reverse_lazy('movie_list')
