# Generated by Django 3.1.2 on 2020-10-09 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0012_auto_20201009_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gathering',
            name='name5',
            field=models.CharField(max_length=230),
        ),
        migrations.AlterField(
            model_name='gathering',
            name='place5',
            field=models.CharField(max_length=230),
        ),
    ]
