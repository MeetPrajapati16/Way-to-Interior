
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [

    
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('confirm_password', views.confirm_password, name='confirm_password'),
    path('', views.index, name='index'),
    path('add_requirements', views.add_requirements, name='add_requirements'),
    path('designers', views.designers, name='designers'),
    path('designs', views.designs, name='designs'),
    path('navbar', views.navbar, name='navbar'),
    path('contact', views.contact, name='contact'),
    path('review', views.review, name='review'),


    # path('signup', views.signup, name='signup'),
    path('success', views.success, name='success'),
    path('add_designer', views.add_designer, name='add_designer'),
     path('add-design', views.add_design, name='add_design'),



   








]