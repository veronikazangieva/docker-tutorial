# Generated by Django 2.1.3 on 2018-12-14 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='twit',
            new_name='parent',
        ),
    ]
