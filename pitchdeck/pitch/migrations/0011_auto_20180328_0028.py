# Generated by Django 2.0.1 on 2018-03-27 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pitch', '0010_auto_20180320_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Userprofile',
        ),
    ]