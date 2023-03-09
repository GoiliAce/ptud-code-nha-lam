from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path('cv1', views.cv1,name='cv1'),
    path('cv2',views.cv2, name='cv2'),
    path('todo1',views.todo1, name='todo1'),
    path('todo2',views.todo2, name='todo2'),
]