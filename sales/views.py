from django.shortcuts import render


# Create your views here.
def sales_page(request):
    context = {}
    return render(request, 'sales_management/sales.html', context)
