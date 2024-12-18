from rest_framework.serializers import ModelSerializer
from products.models import Products, Category, Order
from users.models import User

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'