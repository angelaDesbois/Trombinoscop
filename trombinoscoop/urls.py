"""trombinoscoop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from trombi.views import welcome, login, register, add_friend, show_profile, modify_profile, logout
from django.contrib import admin
from trombi.views import ajax_check_email_field, ajax_add_friend


urlpatterns = [
    url('^$', welcome),
    url('^login$', login),
    url('^logout$', logout),
    url('^welcome$', welcome),
    url('^register$', register),
    url('^addFriend$', add_friend),
    url('^showProfile$', show_profile),
    url('^modifyProfile$', modify_profile),
    url('^ajax/checkEmailField$', ajax_check_email_field),
    url('^ajax/addFriend$', ajax_add_friend),
    url('^admin/', admin.site.urls)
] 
