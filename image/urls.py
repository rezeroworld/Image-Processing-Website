from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('floutage/', views.floutage, name='floutage'),
    path('inversion/', views.inversion, name='inversion'),
]