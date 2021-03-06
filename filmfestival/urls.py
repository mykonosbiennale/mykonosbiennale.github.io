from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from filmfestival import views

urlpatterns = patterns('',
    
    url(r'^selected/(?P<what>[^/]+)/$', 'filmfestival.views.selected', name='selected'),
    url(r'^selected/$', 'filmfestival.views.selected', name='selected'),
    url(r'^send_emails/$', 'filmfestival.views.send_emails', name='send_emails'),                   
    url(r'^films/$', views.FilmList.as_view(), name='film-list'),
    url(r'^film/$', views.FilmList.as_view(), name='film'),
    #url(r'^dramatic-nights/$', views.DramaticNightsFilms.as_view(), name='film-list'),
    url(r'^(?P<year>[0-9]+)/(?P<project>[^/]+)/$', views.FilmProjectList.as_view(), name='film-list'),
    url(r'^program/(?P<slug>[^/]+)/$', views.ProgramDetail.as_view(), name='program'),
    url(r'^(?P<project>[^/]+)/$', views.FilmProjectList.as_view(), name='film-list'),
    #url(r'^video-graffiti/$', views.VideoGraffitiFilms.as_view(), name='video-graffiti'),
    url(r'^documentaries/$', views.DocumentaryFilms.as_view(), name='documentaries'),
    url(r'^film/(?P<slug>[^/]+)/$', views.FilmDetail.as_view(), name='film-detail'),

    url('^who-is-coming/', views.WhoIsComing.as_view(), name='who-is-coming'),
    url('^missing-media/', views.MissingMedia.as_view(), name='missing-media'),
                       #url(r'^film/(?P<slug>[^/]+)/$', cache_page(60 * 15)(views.FilmDetail.as_view()), name='film-detail'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)