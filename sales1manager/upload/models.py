from distutils.command.upload import upload
from enum import auto
from django.db import models
from signup.models import User

# Create your models here.

class Document(models.Model):
    file_id = models.BigAutoField(primary_key=True)
    file_path = models.FileField(upload_to='upload_files/%Y%m%d/')
    file_name = models.CharField(max_length = 200)
    file_user = models.ForeignKey(User, on_delete = models.CASCADE)
    file_create_time = models.DateTimeField(auto_now_add = True)
    file_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.file_name}] [{self.file_user}] [updated at: {self.file_updated_at}]'

    class Meta:
        verbose_name_plural = 'documents_uploaded'
