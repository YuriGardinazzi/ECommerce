from django.core.validators import MinValueValidator
from django.db import models
from user_management.models import CustomUser
from product_management.models import Product
# Create your models here.
class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True, editable=False)
    buyer = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    is_sent = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)])
    total = models.FloatField()
   # producer = models.ForeignKey(CustomUser, on_delete=models.PROTECT)