# Generated by Django 2.0.1 on 2018-03-30 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitch', '0018_auto_20180330_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile',
            new_name='picture',
        ),
    ]