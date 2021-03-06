"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
import django.contrib.auth.views
import secrets.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', django.contrib.auth.views.login, {'template_name': 'login.html', 'redirect_authenticated_user': True}, name='login'),
    url(r'^register/$', secrets.views.register, name='register'),
    url(r'^logout/', django.contrib.auth.views.logout_then_login, name='logout'),
    url(r'^deleteSecret/(?P<id>\d+)$', secrets.views.deleteSecret, name='deleteSecret'),
    url(r'^updateSecret/(?P<id>\d+)$', secrets.views.updateSecret, name='updateSecret'),
    url(r'^mySecrets/$', secrets.views.mySecrets, name='mySecrets'),

]
