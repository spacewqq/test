# Generated by Django 4.1.6 on 2023-04-30 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0027_grade_paper_title_grade_paper_type_alter_grade_paper_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='s_grade',
            field=models.IntegerField(default=0, null=True, verbose_name='总分'),
        ),
        migrations.AlterField(
            model_name='record',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='记录时间'),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
