# Generated by Django 5.0.6 on 2024-06-14 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
    ]
