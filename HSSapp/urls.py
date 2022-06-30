from django.conf.urls import url
from django.shortcuts import render
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.Register.as_view(), name='register'),
    path('profile', views.profileview, name='profile'),
    path('location', views.locationview, name='location'),
    path('locationview', views.Locationview, name='locationview'),
    path('profileview', views.Profileview, name='profileview'),
    path('login', views.loginview, name='login'),
    path('logout', views.logoutview, name='logout'),
    path('', lambda request: render(request, 'home.html'), name='home'),
    path('index', lambda request: render(request, 'index.html'), name='index'),
    path('home', lambda request: render(request, 'home.html'), name='home'),
    path('about', lambda request: render(request, 'about.html'), name='about'),
    path('mypage', views.mypagenotice, name='mypage'),
    path('search', views.search, name='search'),
    path('filter', views.sort, name='filter'),
    path('phoneedit/<int:pk>', views.phoneedit, name='phoneedit'),
    path('jobedit/<int:pk>', views.jobedit, name='jobedit'),
    path('profiledelete/<int:pk>', views.Profiledelete.as_view(), name='profiledelete'),
    path('userview/<int:pk>', views.userview, name='userview'),
    path('locationupdate/<int:pk>', views.Locationupdate.as_view(), name='locationupdate'),
    path('work',views.workrequest,name='work'),
    path('workposted',views.workposted,name='workposted'),
    path('notice',views.notificationview,name='notice'),
    path('notice2/<int:pk>',views.Notice.as_view(),name='notice2'),
    path('deletenotice/<int:pk>',views.Noticedelete.as_view(),name='deletenotice'),
    path('noticedelete/<int:pk>', views.noticedelete, name='deletenotice'),
    path('chat/<int:pk>',views.chat,name='chat'),


]
