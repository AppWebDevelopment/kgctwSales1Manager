from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.calculate, name='calculate_do'),
   path('daily', views.showDaily, name='show_daily'),
   path('dailycalculate', views.calculateDaily, name='calculate_daily'),
]
