from select import select
from turtle import update
from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('', Login),
    path('select',Select,name='selectop'),
    path('add',Add,name='add'),
    path('show',Showbook,name='show'),
    path('addbook',Addbook,name='addbook'),
    path('deletebook',Deletebook,name='deletebook'),
    path('delete/<int:id>',Delete,name='delete'),
    path('editbook',Edit,name='editbook'),
    path('update/<int:id>',Update,name='update'),
    path('editpage/<int:pk>',Editpage,name="editpage"),

]
