from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Stock, User_app
from .serializers import StockSaleSerializer
from .models import StockSale
from datetime import datetime
from decimal import Decimal

class StockSales(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, stock_id):  # Update parameter name here
        sold_shares = request.data.get("sold_shares")

        try:
            stock = Stock.objects.get(id=stock_id)  # Use stock_id to fetch the stock
        except Stock.DoesNotExist:
            return Response("Stock not found", status=HTTP_400_BAD_REQUEST)

        if sold_shares <= 0:
            return Response("Invalid number of shares", status=HTTP_400_BAD_REQUEST)
        
        if stock.total_shares < sold_shares:
            return Response("Not enough shares to sell", status=HTTP_400_BAD_REQUEST)

        sell_price = Decimal(request.data.get("sell_price")) 
        gain = sell_price * sold_shares  

        stock_sale = StockSale.objects.create(
            user=request.user,
            stock=stock,
            sold_shares=sold_shares,
            sell_price=sell_price,
            sell_date=request.data.get("sell_date")
        )

        # Update total shares
        stock.total_shares -= sold_shares
        stock.save()

        # Calculate date spread and gain type
        sell_date_str = request.data.get("sell_date")
        buy_date = stock.date_bought

        try:
            sell_date = datetime.strptime(sell_date_str, "%Y-%m-%d").date()
        except ValueError:
            return Response("Invalid sell_date format", status=HTTP_400_BAD_REQUEST)

        user = request.user
        
        if buy_date:
            date_spread = (sell_date - buy_date).days
            capital = stock.price_at_purchase * sold_shares
            value = (gain - capital)
            if date_spread >= 365 and value > 0:
                user.long_term_gains += value
            elif date_spread <=364 and value > 0:
                user.short_term_gains += value
            else:
                user.losses += value
            user.contributed_capital -= capital
            user.save()
        else:
            stock_sale.capital_gain_type = "Date information missing"
            stock_sale.save()
            
        serializer = StockSaleSerializer(stock_sale)
        return Response(serializer.data, status=HTTP_201_CREATED)


class SoldStockList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, ticker):
        return get_object_or_404(StockSale, ticker=ticker)

    def get(self, request, ticker=None):
        if ticker:
            stock_sale = self.get_object(ticker)
            serializer = StockSaleSerializer(stock_sale)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            user = request.user
            sold_stocks = StockSale.objects.filter(user=user)
            if sold_stocks.exists():
                serializer = StockSaleSerializer(sold_stocks, many=True)
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                return Response("No sold stocks found", status=HTTP_204_NO_CONTENT)

    def put(self, request, ticker):
        stock_sale = self.get_object(ticker)
        if stock_sale:
            serializer = StockSaleSerializer(stock_sale, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response("Stock sale not found", status=HTTP_400_BAD_REQUEST)

    def delete(self, request, ticker):
        stock_sale = self.get_object(ticker)
        if stock_sale:
            stock_sale.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response("Stock sale not found", status=HTTP_400_BAD_REQUEST)
    
class AllStockSalesList(APIView):
    def get(self, request):
        all_stock_sales = StockSale.objects.all()  
        serializer = StockSaleSerializer(all_stock_sales, many=True)
        return Response(serializer.data, status=HTTP_200_OK)