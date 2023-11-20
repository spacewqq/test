# Generated by Django 4.1.6 on 2023-04-08 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_rename_paper_id_record_paper_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionbank',
            name='chapter',
            field=models.CharField(default=1, max_length=40, verbose_name='章节'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='difficulty',
            field=models.CharField(choices=[('easy', '易'), ('middle', '中'), ('difficult', '难')], max_length=10, verbose_name='难度'),
        ),
    ]