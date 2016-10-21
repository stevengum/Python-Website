from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.travels, name="home"),       #MAIN PAGE/FIRST PAGE AFTER LOGIN
    url(r'^add$', views.new_trip, name="new_trip"),
    url(r'^add_trip$', views.add_trip, name="add_trip"),
    url(r'^destinations/(?P<trip_id>\d+)/$', views.destination, name="destination"),
    url(r'^join_trip/(?P<trip_id>\d+)$', views.join_trip, name="join_trip")
]
