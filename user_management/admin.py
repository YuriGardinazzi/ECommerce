from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from product_management.models import Product


class CustomAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login','is_vendor', 'is_admin')
    search_field = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CustomUser, CustomAdmin)
admin.site.register(Product)
