from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')





