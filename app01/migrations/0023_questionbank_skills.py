# Generated by Django 4.1.6 on 2023-04-24 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0022_alter_record_answer_alter_record_c_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionbank',
            name='skills',
            field=models.CharField(default=0, max_length=64, verbose_name='知识点'),
        ),
    ]
