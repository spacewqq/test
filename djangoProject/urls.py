"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from app01 import views  # 添加
from app01.models import Department, UserInfo
from djangoProject import settings
import debug_toolbar
urlpatterns = [
     # path('admin/', admin.site.urls),  #注释掉

    path('index/', views.index),
    path('index2/', views.index2),
    path('user/login/', views.user_login),
    path('user/logout/', views.user_logout),
    path('user/register/', views.user_register),
    path('user/error/', views.user_error),
    path('user/test/', views.user_test),
    path('user/list/', views.user_list),
    path('search/', views.search),
    path('total/problems/', views.total_problems),
    path('user/exam2/', views.user_exam2),
    path('user/', views.user),
    # path('user/exam/', views.user_exam),

    path('user/list/2/', views.user_list_2),


    # path('exams/', views.startExam),
    # path('curriculum/', views.curriculum),
    # path('user/curriculum/', views.user_curriculum),


]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns