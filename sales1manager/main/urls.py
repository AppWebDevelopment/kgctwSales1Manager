from django.urls import path, include
from . import views

urlpatterns = [
   path('index/', views.index, name='main_index'),
   path('', views.loginView, name='main_loginView'),
   path('login/', views.login, name='main_login'),
   path('logout/', views.logout, name='main_logout'),
   path('index/download/', views.download, name='main_download'),
   path('result/', views.result, name='main_result'),
   path('showdaily/', views.showDaily, name='main_show_daily'),
   path('resultdaily/', views.showDaily, name='main_result_daily'),
]
