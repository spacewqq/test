# Generated by Django 4.1.6 on 2023-04-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_record_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testpaper',
            name='answer',
        ),
        migrations.AddField(
            model_name='record',
            name='answer',
            field=models.CharField(default=0, max_length=64, verbose_name='学生答案'),
        ),
    ]