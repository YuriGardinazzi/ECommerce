from django.shortcuts import render
from user_management.models import CustomUser
from django.http import HttpResponse
# Create your views here.

def product_management(request):
    context = {}
    custom_user = CustomUser.objects.all()
    context['custom_user'] = custom_user
    return render(request,'product_setting/product_management', context)