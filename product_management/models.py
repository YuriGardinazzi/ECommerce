from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from user_management.models import CustomUser


# Create your models here.
class MyCategory(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    description = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/')
    price = models.FloatField(validators=[MinValueValidator(0.0001)])
    description = models.TextField(max_length=500)
    quantity = models.PositiveIntegerField(default=1)
    shipment = models.FloatField(default=0, validators=[MinValueValidator(0)])
    producer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(MyCategory,on_delete=models.PROTECT)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    review = models.TextField(max_length=400)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)