# Generated by Django 4.2.6 on 2023-10-31 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_processed',
            field=models.BooleanField(default=False, verbose_name='Обработана'),
        ),
    ]
