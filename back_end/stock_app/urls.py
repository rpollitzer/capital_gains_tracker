from django.urls import path
from .views import StockList, StockDetail

urlpatterns = [
    path("", StockList.as_view(), name="stock-list"),
    path("<int:id>/", StockDetail.as_view(), name="stock-detail"),
    

]