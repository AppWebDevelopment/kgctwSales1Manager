# Generated by Django 2.2.1 on 2022-10-31 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('user_pwd', models.TextField()),
                ('user_name', models.CharField(max_length=30)),
                ('user_level', models.CharField(default='0', max_length=5)),
            ],
        ),
    ]