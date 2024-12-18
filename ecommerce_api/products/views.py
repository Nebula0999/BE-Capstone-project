from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from api.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User
from api.serializers import ProductSerializer, CategorySerializer, UserSerializer, OrderSerializer
from products.models import Products, Order, Category
#from users.models import User

#User = get_user_model
class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductFilter(ModelViewSet):
    queryset = Products.objects.all()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    #filterset_fields = ['products', 'category']
    search_fields = ['products', 'category']
# Create your views here.
