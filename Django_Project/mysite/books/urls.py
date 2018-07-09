from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index' ),
    path('<int:book_id>/', views.detail, name = 'detail')
]
