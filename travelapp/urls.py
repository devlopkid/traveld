from django.urls import path

from travelapp import views

urlpatterns=[
    path('',views.fun,name='fun'),

    path('index', views.index, name='index')

]