from django.conf.urls import url

from . import views

app_name = 'mwserver'

urlpatterns = [

    # ex: /mw/
    url(r'^$', views.index, name='index'),

    # ex: /mw/u/  ?? not needed?  (maybe in admin)
    # ex: /mw/m/  ?? not needed?  (maybe in admin)
    

    # ex: /mw/u/3
    url(r'^u/(?P<id>[0-9]+)/$',
        views.detail_user, name='detail_user'),

    # ex: /mw/m/105
    url(r'^m/(?P<id>[0-9]+)/$',
        views.detail_measurement, name='detail_measurement'),

    # ex: /mw/m/enter/
    url(r'^m/enter/$',
        views.enter_measurement, name='enter_measurement'),

    # ex: /mw/m/post/
    url(r'^m/post/$',
        views.post_measurement, name='post_measurement'),

    # ex: /mw/lm/
    url(r'^lm/$',
        views.report_lametric, name='report_lametric'),
    
]
