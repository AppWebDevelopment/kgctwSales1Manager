from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=200) #사번
    user_pw = models.TextField() #welcome1!
    user_name = models.CharField(max_length=30) #영어이름
    user_validation = models.CharField(default='0', max_length=5) #0 비회원 / 1 일반회원 /2 부장회원 /3 시스템 매니저/ 4 개발자 