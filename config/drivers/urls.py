from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^drivers/', views.submit_driver, name="submit_driver"),
    url(r'^alldrivers/', views.list_drivers, name="list_drivers")
]
