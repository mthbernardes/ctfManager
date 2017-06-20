"""escutador URL Configuration

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
from django.conf.urls import url,include
from challenges import views

urlpatterns = [
    url(r'^manager/ctf/challenges$', views.challenges,name='challenges'),
    url(r'^manager/ctf/challenge/register$', views.challengeRegister,name='challengeRegister'),
    url(r'^manager/ctf/challenge/edit/(?P<challenge_id>\d+)$', views.challengeEdit,name='challengeEdit'),
    url(r'^manager/ctf/challenge/delete/(?P<challenge_id>\d+)$', views.challengeDelete,name='challengeDelete'),
    url(r'^manager/ctf/challenge/download/(?P<challenge_id>\d+)$', views.challengeDownload,name='challengeDownload'),
]
