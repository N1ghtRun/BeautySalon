# Generated by Django 4.1.7 on 2023-04-06 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_alter_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='time',
            field=models.TimeField(),
        ),
    ]