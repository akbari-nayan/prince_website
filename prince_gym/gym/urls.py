from django.contrib import admin
from django.urls import path
from . import views


app_name = 'gym'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('sign_up/', views.register, name='register'),
    path('galary/', views.galary, name='galary'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),

]
