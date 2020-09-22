from django.contrib import admin
from .models import Purchase
# Register your models here.
# Register your models here.
class CustomPurchase(admin.ModelAdmin):
    list_display = ('id','product', 'date','quantity' ,'total', 'is_sent')
    search_field = ('date', 'product')
    # readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Purchase,CustomPurchase)