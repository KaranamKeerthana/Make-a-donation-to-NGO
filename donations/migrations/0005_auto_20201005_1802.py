# Generated by Django 3.1.2 on 2020-10-05 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0004_volunteer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='district1',
            new_name='district2',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='email1',
            new_name='email2',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='name1',
            new_name='name2',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='password1',
            new_name='password2',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='username1',
            new_name='username2',
        ),
    ]
