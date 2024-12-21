from rest_framework.routers import DefaultRouter
from django.urls import path
from products.views import ProductViewSet, CategoryViewSet, UserViewSet, OrderViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()

router.register('products', ProductViewSet)
router.register('users', UserViewSet)
router.register('orders', OrderViewSet)
router.register('category', CategoryViewSet)
#router.register('search', ProductFilter, basename='product_filter')

urlpatterns = [path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),] + router.urls
