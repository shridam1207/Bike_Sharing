from django.urls import path
from . import views


urlpatterns =[
    path("",views.home,name='home'),
    path("slider/",views.slider,name='slider'),
    path("tiles/",views.tiles,name='tiles'),
]