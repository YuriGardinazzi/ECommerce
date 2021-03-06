from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Purchase
from product_management.models import Product


# Create your views here.
@login_required
def sales_page(request):
    context = {}
    return render(request, 'sales_management/sales.html', context)


@login_required
def orders(request):
    context = {}
    return render(request, 'sales_management/orders.html', context)


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
        for product in vendor_products:
            sales = Purchase.objects.filter(product=product).values()
            data.append(list(sales))

        return JsonResponse({'purchase_list': list(data)}, safe=False)
    return JsonResponse(data)


def get_all_orders(request):
    data = {'success': False}
    if request.method == 'POST':
        data = []
        user_id = request.POST.get('user_id')
        orders = Purchase.objects.filter(buyer_id=user_id).values()
        # data.append(list(orders))

        return JsonResponse({'purchase_list': list(orders)}, safe=False)
    return JsonResponse(data)


def send_product(request):
    data = {'success': False}
    if request.method == 'POST':
        purchase_id = request.POST.get('purchase_id')
        print('purchase id', purchase_id)
        purchase = Purchase.objects.get(id=purchase_id)
        purchase.is_sent = True
        purchase.save()
        data['success'] = True
        return JsonResponse(data)
    return JsonResponse(data)


def send_received_confirm(request):
    data = {'success': False}
    if request.method == 'POST':
        purchase_id = request.POST.get('purchase_id')
        print('purchase id', purchase_id)
        purchase = Purchase.objects.get(id=purchase_id)
        purchase.is_received = True
        purchase.save()
        data['success'] = True
        return JsonResponse(data)
    return JsonResponse(data)
