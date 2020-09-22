from django.urls import path, include
from product_management import views
from django.contrib.auth.decorators import login_required
from . import views
app_name = "sales"
urlpatterns = [
    path('sales', views.sales_page, name="sales_page"),
    path('orders', views.orders, name="user_orders"),
    path('ajax/get_orders',views.get_all_orders, name ="get_orders"),
    path('ajax/get_sales',views.get_all_sales, name="get_sales"),
    path('ajax/purchase', views.purchase_product,name="purchase")
]
