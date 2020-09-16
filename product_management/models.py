from django.db import models
from user_management.models import CustomUser


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/')
    price = models.FloatField()
    discount = models.FloatField(default=0)
    description = models.TextField(max_length=2000)
    available = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    producer = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def get_discounted_price(self):
        return self.price - self.price*self.discount
