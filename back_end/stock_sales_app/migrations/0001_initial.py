# Generated by Django 4.2.4 on 2023-08-15 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock_app', '0005_remove_stock_sell_date_remove_stock_sell_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_date', models.DateField()),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=14)),
                ('sold_shares', models.PositiveIntegerField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_app.stock')),
            ],
        ),
    ]
