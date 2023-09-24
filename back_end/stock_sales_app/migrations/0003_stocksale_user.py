# Generated by Django 4.2.4 on 2023-08-16 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_sales_app', '0002_alter_stocksale_sell_date_alter_stocksale_sell_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocksale',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
