# Generated by Django 2.0.1 on 2018-03-27 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitch', '0013_auto_20180328_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(null=True),
        ),
    ]
