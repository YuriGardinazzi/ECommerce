from django.conf import  settings
from django.conf.urls import static
from django.urls import path, include
from . import views
app_name = "product_management"
urlpatterns = [
    path('management', views.product_management, name='product_management'),
]