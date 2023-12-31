# Generated by Django 4.1.6 on 2023-04-22 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_remove_testpaper_answer_record_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('answer', models.CharField(default=0, max_length=64, verbose_name='学生答案')),
                ('grade', models.FloatField(verbose_name='学生得分')),
                ('c_time', models.DateTimeField(verbose_name='记录时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_course', to='app01.course', verbose_name='考试科目')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_paper', to='app01.testpaper', verbose_name='试卷')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_question', to='app01.questionbank', verbose_name='题目')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_id', to='app01.user', verbose_name='学号')),
            ],
            options={
                'verbose_name': '学生成绩',
                'verbose_name_plural': '学生成绩',
            },
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]
