# Generated by Django 3.1.4 on 2021-09-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_trip_driver_rider'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
