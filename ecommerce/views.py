from django.http import JsonResponse
from django.shortcuts import render
from user_management.models import CustomUser
from product_management.models import MyCategory, Product
from sales.models import Purchase
from numpy import dot
from numpy.linalg import norm
import numpy as np


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


def get_search(request):
    context = {}
    if request.method == 'POST':
        query = request.POST['query']
        category = request.POST['category']
        if category == 'all' and query == '':
            products = Product.objects.all()
            context['products'] = products
        elif category != 'all' and query == '':
            products = Product.objects.filter(category_id=category)
            context['products'] = products
        elif category == 'all':
            print(" category all - query presente")
            products = Product.objects.filter(name__contains=query)
            context['products'] = products
        else:
            products = Product.objects.filter(name__contains=query, category_id=category)
            context['products'] = products
    items = []
    if(request.user.is_authenticated):
        suggested_items = get_similary_items(request.user.id)
        if(suggested_items):
            for element in suggested_items:
                items.append(Product.objects.get(id=element))

    context['suggested_items'] = items
    return render(request, 'search.html', context)


def get_categories(request):
    data = {'success': False}
    if request.method == 'POST':
        categories = MyCategory.objects.all().values()
        data = {'categories': list(categories)}
    return JsonResponse(data, safe=False)





def jaccard(im1, im2):
    """
    Computes the Jaccard metric, a measure of set similarity.
    Parameters
    ----------
    im1 : array-like, bool
        Any array of arbitrary size. If not boolean, will be converted.
    im2 : array-like, bool
        Any other array of identical size. If not boolean, will be converted.
    Returns
    -------
    jaccard : float
        Jaccard metric returned is a float on range [0,1].
        Maximum similarity = 1
        No similarity = 0

    Notes
    -----
    The order of inputs for `jaccard` is irrelevant. The result will be
    identical if `im1` and `im2` are switched.
    """
    im1 = np.asarray(im1).astype(np.bool)
    im2 = np.asarray(im2).astype(np.bool)

    if im1.shape != im2.shape:
        raise ValueError("Shape mismatch: im1 and im2 must have the same shape.")

    intersection = np.logical_and(im1, im2)

    union = np.logical_or(im1, im2)

    return intersection.sum() / float(union.sum())


def get_similary_items(id):
    data = {}
    list = CustomUser.objects.exclude(id=id)
    users = list.values('id')
    products = Product.objects.values('id')

    dim_users = len(users)
    dim_products = len(products)
    matrix = np.zeros((dim_users, dim_products))
    input_user_vector = np.zeros((1, dim_products))

    #set the boolean matrix
    for i in range(dim_users):
        for j in range(dim_products):
            purchase = Purchase.objects.filter(buyer_id=users[i]['id'], product_id=products[j]['id'])
            if purchase:
                matrix[i][j] = 1.0
            else:
                matrix[i][j] = 0.0

    #set the boolean user vector
    for i in range(dim_products):
        purchase = Purchase.objects.filter(buyer_id=id, product_id=products[i]['id'])
        if purchase:
            input_user_vector[0][i] = 1.0
        else:
            input_user_vector[0][i] = 0.0

    max = 0.0
    pos = 0
    list_id_to_retrieve = []

    #Get the Row with the highest jaccard coeff
    for i in range(dim_users):
        jacc_coeff = jaccard(matrix[i][:], input_user_vector[0][:])
        if (jacc_coeff > max):
            pos = i
            max = jacc_coeff

    #add to the list the items that are present in the row with the highest jaccard coeff
    #that the user never bought
    for i in range(dim_products):
        if((matrix[pos][i]-input_user_vector[0][i]) == 1):
            list_id_to_retrieve.append(products[i]['id'])

    return list_id_to_retrieve


