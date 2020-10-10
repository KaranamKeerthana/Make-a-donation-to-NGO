# Generated by Django 3.1.2 on 2020-10-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0014_auto_20201009_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name4',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='gathering',
            name='cause5',
            field=models.CharField(max_length=920),
        ),
        migrations.AlterField(
            model_name='gathering',
            name='name5',
            field=models.CharField(max_length=330),
        ),
        migrations.AlterField(
            model_name='gathering',
            name='place5',
            field=models.CharField(max_length=330),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='district',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='name',
            field=models.CharField(max_length=330),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='public',
            name='district1',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='public',
            name='email1',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='public',
            name='name1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='public',
            name='username1',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='district2',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='email2',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='name2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='username2',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]