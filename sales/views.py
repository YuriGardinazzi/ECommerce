from django.http import JsonResponse
from django.shortcuts import render
from .models import Purchase
from product_management.models import Product


# Create your views here.
def sales_page(request):
    context = {}
    return render(request, 'sales_management/sales.html', context)


def purchase_product(request):
    data = {'success': False}
    if request.method == 'POST':
        purchase = Purchase()
        purchase.product_id = request.POST.get('product_id')
        purchase.buyer_id = request.POST.get('user_id')
        purchase.quantity = int(request.POST.get('quantity'))
        product = Product.objects.get(id=purchase.product_id)

        if product.quantity < purchase.quantity:
            return JsonResponse(data)
        product.quantity -= purchase.quantity
        product.save()

        purchase.total = purchase.quantity * product.price + product.shipment
        purchase.save()
        data = {'success': True}

    return JsonResponse(data)


def get_all_sales(request):
    data = {'success': False}
    if request.method == 'POST':
        vendor_id = request.POST.get('producer_id')
        vendor_products = Product.objects.filter(producer_id=vendor_id)
        data = []
        print(vendor_products)
        for product in vendor_products:
            sales = Purchase.objects.filter(product=product).values()
            data.append(list(sales))

        return JsonResponse({'purchase_list': list(data)}, safe=False)
    return JsonResponse(data)
