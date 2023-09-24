from django.urls import path
from .views import StockSales, SoldStockList, AllStockSalesList

urlpatterns = [
    path('sell-stock/<int:stock_id>/', StockSales.as_view(), name='sell-stock'),
    path('sold-stock/', SoldStockList.as_view(), name='sold-stock-list'),
    path('all-stock-sales/', AllStockSalesList.as_view(), name='all-stock-sales-list'),
]
