# Generated by Django 4.1.6 on 2023-04-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_questionbank_chapter_alter_questionbank_difficulty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='course',
            new_name='course_id',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='paper',
            new_name='paper_id',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RemoveField(
            model_name='questionbank',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='record',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='record',
            name='correct',
        ),
        migrations.AddField(
            model_name='testpaper',
            name='answer',
            field=models.CharField(default=0, max_length=64, verbose_name='学生答案'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='用户ID'),
        ),
    ]
