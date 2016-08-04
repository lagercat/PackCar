from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^driver/', views.submit_driver, name="submit_driver")
]
