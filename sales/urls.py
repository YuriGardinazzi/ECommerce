from django.urls import path, include
from product_management import views
from django.contrib.auth.decorators import login_required
from . import views
app_name = "sales"
urlpatterns = [
    path('sales', views.sales_page, name="sales_page"),
    path('ajax/purchase', views.purchase_product,name="purchase")
]
