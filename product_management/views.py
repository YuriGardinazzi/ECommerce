from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from user_management.models import CustomUser
from django.http import HttpResponse, JsonResponse

from .forms import ProductCrispyForm
from .models import Product, Review
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView


# Create your views here.
# @login_required()
class ProductManagement(ListView):
    model = Product
    template_name = 'product_setting/product_management'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(producer=self.kwargs.get('pk'))


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_setting/detail.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(id=self.kwargs['pk'])


class ProductAdd(CreateView):
    model = Product
    template_name = 'product_setting/add.html'
    form_class = ProductCrispyForm

    # fields = '__all__'
    # fields = ('first_name', 'middle_name', 'last_name')
    # success_url = reverse_lazy('product_management:product_management',kwargs.get('pk'))
    success_url = reverse_lazy('product_management:product_management')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.producer = self.request.user
        obj.save()
        return super(ProductAdd, self).form_valid(form)


class ProductChange(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product_setting/update_product.html'
    form_class = ProductCrispyForm
    success_url = reverse_lazy('product_management:product_management')


def get_vendor_products(request):
    producer = request.POST.get('producer_id')
    products_list = Product.objects.filter(producer=producer).values()
    data = []
    data.append({'products_list': list(products_list)})
    print(data)
    return JsonResponse(data, safe=False)


def delete_element(request):
    productID = request.POST.get('product_id')
    successDeletion = True
    data = []
    try:
        productToDelete = Product.objects.filter(id=productID)
        productToDelete.delete()
    except Product.DoesNotExist:
        print("element ", productID, " not found")
        successDeletion = False
    return JsonResponse({"success": successDeletion})


# ----------------------REVIEWS----------------------
def add_review(request):
    data = {'success': False}
    if request.method == 'POST':
        review = Review()
        review.product_id = request.POST.get('product_id')
        review.review = request.POST.get('review')
        review.rating = request.POST.get('rating')
        review.user_id = request.POST.get('user_id')
        review.save()
        data['success'] = True
    return JsonResponse(data)


def get_all_reviews(request):
    if request.method == 'POST':
        data = []
        product_id = request.POST.get('product_id')
        review_list = Review.objects.filter(product_id=product_id).values()
        data.append({'reviews_list': list(review_list)})
        print(data)
        return JsonResponse(data, safe=False)
    return JsonResponse({"success": False})

def get_average_rating(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        average_rating = Review.objects.filter(product_id=product_id).aggregate(value=Avg('rating'))
        return JsonResponse({'average_rating':average_rating['value']})