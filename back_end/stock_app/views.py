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
from .serializers import StockSerializer

class StockList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stocks = Stock.objects.filter(user=request.user)
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        request.data["user"] = request.user.id
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            stock = serializer.save()

        
        total_value = stock.total_shares * stock.price_at_purchase
        user = request.user
        user.contributed_capital += total_value 
        user.save()

        return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class StockDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Stock.objects.get(id=id, user=self.request.user)
        except Stock.DoesNotExist:
            return None

    def get(self, request, id):
        stock = self.get_object(id)
        if stock:
            serializer = StockSerializer(stock)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response("Stock not found", status=HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        stock = self.get_object(id)
        if stock:
            serializer = StockSerializer(stock, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response("Stock not found", status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        stock = self.get_object(id)
        user = request.user
        if stock:
            capital = stock.price_at_purchase * stock.total_shares
            user.contributed_capital -= capital
            user.save()
            stock.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response("Stock not found", status=HTTP_400_BAD_REQUEST)