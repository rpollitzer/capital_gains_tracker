# Generated by Django 4.2.4 on 2023-08-15 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0004_alter_stock_sell_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='sell_date',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='sell_price',
        ),
    ]
