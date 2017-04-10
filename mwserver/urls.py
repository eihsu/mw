from django.conf.urls import url

from . import views

urlpatterns = [

    # ex: /mw/
    url(r'^$', views.index, name='index'),

    # ex: /mw/u/  ?? not needed?  (maybe in admin)
    # ex: /mw/m/  ?? not needed?  (maybe in admin)
    

    # ex: /mw/u/3
    url(r'^u/(?P<id>[0-9]+)/$',
        views.detail_user, name='details for user'),

    # ex: /mw/m/105
    url(r'^m/(?P<id>[0-9]+)/$',
        views.detail_measurement, name='details for measurement'),

    # ex: /mw/m/enter/
    url(r'^m/enter/$',
        views.enter_measurement, name='entering a measurement'),

]
