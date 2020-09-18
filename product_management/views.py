from django.shortcuts import render
from django.urls import reverse_lazy

from user_management.models import CustomUser
from django.http import HttpResponse

from .forms import ProductCrispyForm
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView


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
        return Product.objects.filter(producer=self.kwargs['pk'])


class ProductAdd(CreateView):
    model = Product
    template_name = 'product_setting/add.html'
    form_class = ProductCrispyForm

    # fields = '__all__'
    # fields = ('first_name', 'middle_name', 'last_name')
    # success_url = reverse_lazy('product_management:product_management',kwargs.get('pk'))

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.producer = self.request.user
        obj.save()
        return super(ProductAdd, self).form_valid(form)

    def get_success_url(self):
        # if you are passing 'pk' from 'urls' to 'DeleteView' for company
        # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
        producer = self.kwargs['pk']
        return reverse_lazy('product_management:product_management', kwargs={'pk': producer})


'''
    context = {}
    custom_user = CustomUser.objects.all()
    context['custom_user'] = custom_user
    return render(request, 'product_setting/product_management', context)
'''
