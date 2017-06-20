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
from users import views

urlpatterns = [
    url(r'^manager/ctf$', views.userLogin,name='userLogin'),
    url(r'^manager/ctf/logout$', views.userLogout,name='userLogout'),
    url(r'^manager/ctf/users$', views.usersView,name='usersView'),
    url(r'^manager/ctf/user/register$', views.userRegister,name='userRegister'),
    url(r'^manager/ctf/user/changepassword$', views.userPassword,name='userPassword'),
    url(r'^manager/ctf/user/edit/(?P<sysuser_id>\d+)$', views.userEdit,name='userEdit'),
    url(r'^manager/ctf/`user/delete/(?P<sysuser_id>\d+)$', views.userDelete,name='userDelete'),
]
