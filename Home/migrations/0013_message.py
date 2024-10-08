# Generated by Django 5.0.6 on 2024-07-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_otherimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('name', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
