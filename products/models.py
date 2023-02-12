from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = RichTextField(blank=True, null=True, max_length=2000)

    class Meta:
        verbose_name = 'Продукция Категории'
        verbose_name_plural = 'Продукции Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = RichTextField(max_length=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукции'

