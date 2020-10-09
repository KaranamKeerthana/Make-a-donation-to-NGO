# Generated by Django 3.1.2 on 2020-10-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
            ],
        ),
    ]
