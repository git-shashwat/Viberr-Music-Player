from django.urls import path, re_path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('',views.IndexView.as_view(), name='index'),
        
    #register/
    re_path(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /music/69
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    re_path(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    
    # /music/album/2/
    re_path(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/album/3/addsong/
    re_path(r'album/addsong/$', views.SongCreate.as_view(), name='song-add'),

    # /music/songs/
    path('songs/', views.SongView.as_view(), name='song-view'),

    # /music/songs/3/delete
    re_path(r'songs/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song-delete'),

    # /music/filter_basis=genre_field&search_query=Rap#
    re_path(r'^search_result/$', views.FilterView, name='album-filter'),

]