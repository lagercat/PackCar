from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^packages/', views.submit_package, name="submit_package"),
    url(r'^allpackages/', views.list_packages, name="list_packages")
]
