from rest_framework import serializers
from .models import StockSale

class StockSaleSerializer(serializers.ModelSerializer):
    stock_ticker = serializers.CharField(source='stock.ticker', read_only=True)

    class Meta:
        model = StockSale
        fields = ['stock', 'stock_ticker', 'sell_date', 'sell_price','user']