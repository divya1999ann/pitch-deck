# Generated by Django 2.0.1 on 2018-03-30 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitch', '0019_auto_20180330_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='PROJECT_PATH/static'),
        ),
    ]
