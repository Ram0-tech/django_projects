from django import forms


# class MovieForm(forms.Form):
#     image = forms.ImageField()
#     movie_name = forms.CharField()
#     language = forms.CharField()
#     director = forms.CharField()
#     year = forms.IntegerField()
#     description = forms.CharField(widget=forms.Textarea)


from movie.models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"