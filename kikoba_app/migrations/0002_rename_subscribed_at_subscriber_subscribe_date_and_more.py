# Generated by Django 4.1.7 on 2023-04-23 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kikoba_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='subscribed_at',
            new_name='subscribe_date',
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
    ]
