# Generated by Django 4.2.4 on 2023-08-17 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0006_alter_stock_total_shares'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='total_shares',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
