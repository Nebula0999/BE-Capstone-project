from django.db import models
from django.core.exceptions import ValidationError

#def validate_value(value):
    #if value is not True:
        #raise ValidationError ("Field is required")
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Products(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=255)
    price = models.DecimalField(blank=False)
    category = models.ForeignKey(Category, related_name='type', on_delete=models.CASCADE)
    stock_Quantity = models.IntegerField(blank=False)
    image_URL = models.URLField()
    created_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




# Create your models here.
