# Generated by Django 4.1.6 on 2023-04-30 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0026_alter_record_course_alter_record_paper_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='paper_title',
            field=models.CharField(default='第一章测试', max_length=64, verbose_name='试卷名称'),
        ),
        migrations.AddField(
            model_name='grade',
            name='paper_type',
            field=models.CharField(default='固定试卷', max_length=64, verbose_name='试卷类型'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_paper', to='app01.record', verbose_name='题目'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='sid',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='s_id', to='app01.user', verbose_name='学号'),
        ),
    ]