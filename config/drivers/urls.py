from django.conf.urls import url
from django import views

urlpatterns = [
    url(r'^driver/', views.submit_driver, name="submit_driver")
]
