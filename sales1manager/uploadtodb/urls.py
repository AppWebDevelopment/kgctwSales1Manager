from django.urls import path, include
from . import views

urlpatterns = [
   path('daily/', views.dailyToDB, name='daily_to_db'),
   path('monthly/', views.monthlyToDB, name='monthly_to_db'),
   path('yearly/', views.yearlyToDB, name='yearly_to_db'),
   path('store/', views.storeInfoToDB, name='storeinfo_to_db'),
]
