from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^packages/', views.submit_package, name="submit_package"),
    url(r'^allpackages/', views.list_packages, name="list_packages"),
    url(r'^manager/', views.manager, name="manager"),
    url(r'^accept/(?P<slug>[^\.]+)/$', views.accept, name="accept"),
    url(r'^decline/(?P<slug>[^\.]+)/$', views.decline, name="decline"),
    url(r'^finish/(?P<slug>[^\.]+)/$', views.finish, name="finish"),
    url(r'^package/(?P<slug>[^\.]+)/$', views.package, name='package'),
    url(r'^edit_package/(?P<slug>[^\.]+)/$', views.edit_package, name='edit_package'),
]
