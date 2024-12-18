from django.contrib import admin
from .models import Products, Category, Order

class OrderAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Products)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
# Register your models here.
