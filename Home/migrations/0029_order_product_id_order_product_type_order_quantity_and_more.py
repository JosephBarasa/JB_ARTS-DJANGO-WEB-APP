# Generated by Django 5.0.6 on 2024-07-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0028_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='product_type',
            field=models.CharField(choices=[('canvas', 'Canvas'), ('bottle', 'Bottle')], default='art', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
