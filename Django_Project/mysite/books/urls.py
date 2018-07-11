from django.contrib import admin
from django.urls import path
from . import views

app_name = 'books' #namespaces in Django

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index' ),
    path('(?P<pk>[0-9]+)/', views.DetailView.as_view(), name = 'detail'),
    path('books/add/',views.BookCreate.as_view(), name = 'book-add'),
]
