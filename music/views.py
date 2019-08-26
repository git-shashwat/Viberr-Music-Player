from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .models import Album, Song
from django.http import HttpResponse

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class SongView(generic.ListView):
    template_name = 'music/songView.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/albumDetail.html'
   
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class SongCreate(CreateView):
    model = Song
    fields = ['album','song_file', 'file_type', 'song_title', 'is_favorite']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:song-view')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # displays a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

        # returns User objects if credentials are correct
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return HttpResponse(user.username + " Is now logged in.")

        else:
            return render(request, self.template_name, context={'form': form})

def FilterView(request):
    template_name = 'music/index.html'
    filter_basis = request.GET['filter_basis']
    search_query = request.GET['search_query']
    context = Album.objects.filter(**{filter_basis : search_query.upper()})

    if len(context) != 0:
        return render(request, template_name, {'all_albums' : context})
    else:
        return render(request, 'music/unavailable.html', {})