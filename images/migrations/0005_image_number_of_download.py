# Generated by Django 3.2.7 on 2021-09-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_image_amount_made'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='number_of_download',
            field=models.IntegerField(default=0),
        ),
    ]