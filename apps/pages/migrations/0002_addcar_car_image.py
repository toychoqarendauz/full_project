# Generated by Django 4.2.2 on 2023-06-29 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcar',
            name='car_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
