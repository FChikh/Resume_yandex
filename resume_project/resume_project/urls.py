"""resume_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import django.views.static

from resume_project import settings
import django.views.static

from resume import views, auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.signin_site_page),
    path('register/', auth_views.register),
    path('logout/', views.logout_func),
    path('', views.main),
    path('test/', views.test),
    path('swift/', views.test_for_swift_app),
    path('test_pictures/', views.test_pictures)
]

if settings.DEBUG == False:
    urlpatterns += url(r'^static/(?P<path>.*)$', django.views.static.serve,
                       {'document_root': settings.STATIC_URL, 'show_indexes': settings.DEBUG}),
