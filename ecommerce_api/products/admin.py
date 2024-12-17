from django.contrib import admin
from .models import Products, Category

admin.site.register(Products, Category)
# Register your models here.
