from django.conf import  settings
from django.conf.urls import static
from django.urls import path, include
from product_management import views
from django.contrib.auth.decorators import login_required
app_name = "product_management"
urlpatterns = [
    path('management/', login_required(views.ProductManagement.as_view()), name='product_management'),
    path('management/<int:pk>/detail', views.ProductDetail.as_view(), name='product_detail'),
    path('management/add', views.ProductAdd.as_view(),name='product_add'),
    path('management/<int:pk>/change', views.ProductChange.as_view(), name='edit_product'),

    path('ajax/add_review', views.add_review, name='add_review'),
    path('ajax/review_list', views.get_all_reviews, name='review_list'),
    path('ajax/get_average_ratings', views.get_average_rating, name='average_rating'),
    path('ajax/product_list',views.get_vendor_products, name='product_list'),
    path('ajax/delete_product',views.delete_element, name='delete_product')
]