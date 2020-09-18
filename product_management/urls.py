from django.conf import  settings
from django.conf.urls import static
from django.urls import path, include
from product_management import views
from django.contrib.auth.decorators import login_required
app_name = "product_management"
urlpatterns = [
    path('management/<int:pk>', login_required(views.ProductManagement.as_view()), name='product_management'),
    path('management/<int:pk>/detail', views.ProductDetail.as_view(), name='product_detail'),
    path('management/add', views.ProductAdd.as_view(),name='product_add'),
]