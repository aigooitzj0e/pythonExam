from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reg_process$', views.reg_process),
    url(r'^login_process$', views.login_process),
    url(r'^dashboard/$', views.dashboard),
    url(r'^logout/$', views.logout),
    url(r'^addTravel/$', views.addTravel),
    url(r'^addTravel_process$', views.addTravel_process),
    # url(r'^dashboard/delete/(?P<id>\d+)$', views.delete),
    url(r'^join/(?P<tid>\d+)$', views.join),
    url(r'^show/(?P<tid>\d+)$', views.show),
]
