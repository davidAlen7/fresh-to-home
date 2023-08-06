
from django.urls import path,include
from . import views

urlpatterns = [
    path('freshtohome/',views.home,name='home'),
    path('freshtohome/conditions/',views.conditions,name='conditions'),
    path('freshtohome/about/',views.about,name='about'),
    path('freshtohome/contact/',views.contact,name='contact'),
]
