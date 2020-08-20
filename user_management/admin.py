from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person, CustomUser

# Register your models here.
admin.site.register(Person)


class CustomAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_field = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CustomUser, CustomAdmin)
