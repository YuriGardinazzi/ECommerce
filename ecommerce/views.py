from django.http import JsonResponse
from django.shortcuts import render
from user_management.models import CustomUser
from product_management.models import MyCategory, Product


def home(request):
    context = {}
    custom_user = CustomUser.objects.all()
    categories = MyCategory.objects.all()
    last_ten = Product.objects.filter(quantity__gt=0).order_by('-id')[:10]
    print(categories)
    context['custom_user'] = custom_user
    context['categories'] = categories
    context['products'] = last_ten
    return render(request, 'home.html', context)


def get_categories(request):
    if request.method == 'POST':
        categories = MyCategory.objects.all().values()
        print(categories)
        data = {'categories': list(categories)}
    return JsonResponse(data, safe=False)
