from django.shortcuts import render
from requests import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from api.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User
from api.serializers import ProductSerializer, CategorySerializer, UserSerializer, OrderSerializer, OrderItemSerializer
from products.models import Products, Order, Category, OrderItem
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters import FilterSet

class CustomPagination(PageNumberPagination):
    page_size = 10  
#from users.models import User

#User = get_user_model
def ProductsFilter(FilterSet):
    class Meta:
        model = Products
        fields = ['id', 'name']  


class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['products', 'category']

    def get(self, request, *args, **kwargs):
       # Get the filtered queryset
       queryset = self.filter_queryset(self.get_queryset())

       page = self.paginate_queryset(queryset)
       if page is not None:
           serializer = self.get_serializer(page, many=True)
           return self.get_paginated_response(serializer.data)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
    
class OrderItemView(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


class CancelOrderView(APIView):
    def post(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
            if order.status == 'completed':
                return Response({"error": "Cannot cancel a completed order."}, status=status.HTTP_400_BAD_REQUEST)

            for item in order.items.all():
                product = item.product
                product.stock += item.quantity
                product.save()

            order.status = 'canceled'
            order.save()
            return Response({"message": "Order canceled and stock restored."}, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
# Create your views here.
