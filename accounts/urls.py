from django.conf.urls import  include, url
from . import views

# responsavel pelo login ali em baixo
from django.contrib.auth import views as auth_views

urlpatterns = [

  #  url(r'^entrar/$', 'django.contrib.auth.views.login', name='login'),

  	url(r'^$', views.dashboard, name='dashboard'),

    url(r'^entrar/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^cadastrar/$', views.register, name='register'),
    url(r'^sair/$', auth_views.logout, {'next_page': 'core:home'}, name='logout'),

    url(r'^editar/$', views.edit, name='edit'),

    url(r'^editar-senha/$', views.edit_password, name='edit_password'),



    



]