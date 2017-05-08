from django.conf.urls import include, url
from . import views


urlpatterns = [


    #url(r'^$', views.home, name='home'),
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<pk>\d+)/$', views.details, name='details')
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details')

]