from django.db import models
from stock_app.models import Stock
from user_app.models import User_app

class StockSale(models.Model):
    user = models.ForeignKey(User_app, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    sell_date = models.DateField(null=True)
    sell_price = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    sold_shares = models.DecimalField(max_digits=14, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.stock.ticker} - {self.sell_date}"
