# Generated by Django 4.1.6 on 2023-04-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='管理员ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('phone', models.IntegerField(max_length=64, verbose_name='电话')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='学生ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
            ],
        ),
    ]
