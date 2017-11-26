from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.register, name='register'),

    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'feedback/$', views.feedback, name='feedback'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),

    url(r'^create_album/$', views.create_album, name='create_album'),

    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),

    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),

    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),

    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
    
    url(r'^query1/$', views.q1, name='q1'),

    url(r'^query2/$', views.q2, name='q2'),
    
    url(r'^query3/$', views.q3, name='q3'),
        
    url(r'^query4/$', views.q4, name='q4'),
    
    url(r'^query5/$', views.q5, name='q5'),

]
