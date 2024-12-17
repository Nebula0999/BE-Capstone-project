from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from api.serializers import ProductSerializer
class ProductView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = all
# Create your views here.
