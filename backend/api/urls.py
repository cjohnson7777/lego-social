from django.urls import path
from api import views

urlpatterns = [
    path('sets/', views.get_sets),
    path('sets/<str:rid>/', views.get_set)
]