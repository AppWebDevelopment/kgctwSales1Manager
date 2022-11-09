from django.db import models

# Create your models here.

class User(models.Model):
    USER_LEVEL = (
        ('General', 'Lv1'),
        ('Employee', 'Lv2'),
        ('Manager', 'Lv3'),
        ('Admin', 'Lv4'),
    )
    user_id = models.CharField(primary_key=True,max_length=200) #사번
    user_email = models.EmailField(max_length=254) #이메일
    user_pw = models.TextField() #welcome1!
    user_name = models.CharField(max_length=30) #영어이름
    user_validation = models.CharField(default='General', max_length=10, choices = USER_LEVEL)
    user_create_time = models.DateTimeField(auto_now_add = True, null = True)
    user_updated_at = models.DateTimeField(auto_now=True, null = True)

    def __str__(self):
        return f'[{self.user_id}]{self.user_name}:Validation {self.user_validation}'