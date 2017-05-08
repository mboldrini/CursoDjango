"""curso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# responsavel por exibir o link das imagens
from django.conf import settings
from django.conf.urls.static import static

# tem que importar a views primeiro
from core import views

# urls em outro app, no caso o core
from django.conf.urls import include, url

urlpatterns = [

    url(r'^admin/', admin.site.urls),


   # url(r'^$', views.home, name='home'),
   # url(r'^contato/$', views.contact, name='contact')

    # leva para o arquivo urls no app CORE
    # namespace e para poder repetir o nome nas urls
    url(r'^', include('core.urls', namespace='core')),

    url(r'^cursos/', include('courses.urls', namespace='courses')),

    url(r'^conta/', include('accounts.urls', namespace='accounts')),

]


# verifica as imagens se tiver liberado no settings
# ele exibe

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)