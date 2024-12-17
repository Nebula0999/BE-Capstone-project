from rest_framework.serializers import ModelSerializer
from products.models import Products
from users.models import User

class ProductSerializer(ModelSerializer):
    model = Products
    fields = '__all__'