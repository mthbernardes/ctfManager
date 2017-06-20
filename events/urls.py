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
from events import views

urlpatterns = [
    url(r'^manager/ctf/events$', views.events,name='events'),
    url(r'^manager/ctf/event/register$', views.eventRegister,name='eventRegister'),
    url(r'^manager/ctf/event/delete/(?P<event_id>\d+)$', views.eventDelete,name='eventDelete'),
    url(r'^manager/ctf/event/edit/(?P<event_id>\d+)$', views.eventEdit,name='eventEdit'),
    url(r'^manager/ctf/event/challenges/(?P<event_id>\d+)$', views.eventChallenges,name='eventChallenges'),
    url(r'^manager/ctf/event/challenges/(?P<event_id>\d+)/add/(?P<challenge_id>\d+)$', views.eventChallengesAdd,name='eventChallengesAdd'),
    url(r'^manager/ctf/event/challenges/(?P<event_id>\d+)/del/(?P<challenge_id>\d+)$', views.eventChallengesDel,name='eventChallengesDel'),
]
