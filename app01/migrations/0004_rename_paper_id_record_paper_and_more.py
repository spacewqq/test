# Generated by Django 4.1.6 on 2023-04-07 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_course_questionbank_alter_admin_phone_testpaper_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='paper_id',
            new_name='paper',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='question_id',
            new_name='question',
        ),
    ]
