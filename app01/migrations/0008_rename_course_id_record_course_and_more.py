# Generated by Django 4.1.6 on 2023-04-22 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_remove_record_question_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='paper_id',
            new_name='paper',
        ),
    ]