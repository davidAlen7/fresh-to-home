
from django.urls import path,include
from . import views

urlpatterns = [

    path('freshtohome/signup/',views.signup,name='signup'),
    path('freshtohome/login/',views.loginview,name='login'),
    path('freshtohome/logout/',views.logoutview,name='logout'),

]
