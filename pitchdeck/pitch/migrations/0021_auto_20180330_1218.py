# Generated by Django 2.0.1 on 2018-03-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitch', '0020_auto_20180330_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]
