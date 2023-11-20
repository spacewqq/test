# Generated by Django 4.1.6 on 2023-04-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0021_alter_record_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='answer',
            field=models.CharField(default=0, max_length=64, null=True, verbose_name='学生答案'),
        ),
        migrations.AlterField(
            model_name='record',
            name='c_time',
            field=models.DateTimeField(null=True, verbose_name='记录时间'),
        ),
        migrations.AlterField(
            model_name='record',
            name='correct',
            field=models.CharField(max_length=40, null=True, verbose_name='正确答案'),
        ),
        migrations.AlterField(
            model_name='record',
            name='question',
            field=models.CharField(max_length=64, null=True, verbose_name='题目'),
        ),
    ]
