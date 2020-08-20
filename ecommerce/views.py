from django.shortcuts import render
from user_management.models import CustomUser


def home(request):
    context = {}
    custom_user = CustomUser.objects.all()
    context['custom_user'] = custom_user
    return render(request, 'home.html', context)
