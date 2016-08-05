from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^packages/', views.submit_package, name="submit_package"),
    url(r'^allpackages/', views.list_packages, name="list_packages"),
    url(r'^manager/', views.manager, name="manager"),
    url(r'^accept/', views.accept, name="accept"),
    url(r'^package/(?P<slug>[^\.]+)/$', views.package, name='package'),
    url(r'^edit_package/(?P<slug>[^\.]+)/$', views.edit_package, name='edit_package')
]
