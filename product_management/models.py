from django.core.validators import MinValueValidator
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
    #discount = models.FloatField(default=0,validators=[MinValueValidator(0.0)])
    description = models.TextField(max_length=500)
    #available = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    producer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(MyCategory,on_delete=models.PROTECT)

    def get_discounted_price(self):
        return self.price - self.price * self.discount


