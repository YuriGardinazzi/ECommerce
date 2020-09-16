from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, MyCategory


# Register your models here.
class CustomProductDisplay(admin.ModelAdmin):
    list_display = ('producer', 'name', 'price', 'discount', 'category')
    search_field = ('producer', 'name')
    # readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CustomCategoryDisplay(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Product, CustomProductDisplay)
admin.site.register(MyCategory, CustomCategoryDisplay)
