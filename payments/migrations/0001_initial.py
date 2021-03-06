# Generated by Django 3.2.7 on 2021-09-14 14:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0004_image_amount_made'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.UUIDField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('image_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.image')),
            ],
        ),
    ]
