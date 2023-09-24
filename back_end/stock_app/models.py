from django.db import models
from user_app.models import User_app

class Stock (models.Model):
    user = models.ForeignKey(User_app, on_delete=models.CASCADE, related_name="stocks")
    ticker = models.CharField(max_length=5)
    date_bought= models.DateField()
    total_shares= models.DecimalField(max_digits=14, decimal_places=2, null=True)
    price_at_purchase = models.DecimalField(max_digits=14, decimal_places=2)
    
    def __str__(self):
        return f"{self.ticker} - {self.user.email}"