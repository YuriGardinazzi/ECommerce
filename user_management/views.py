from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm, AccountUpdateForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from .models import CustomUser


def user_home(request):
    return render('user_home.html')


class SignUpView(CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_message = 'Success: Person was created.'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        self.object.save()
        return response


def account_view(request):
    if not request.user.is_authenticated:
        return redirect('user_management:login')
    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, request.FILES or None, instance=request.user)
        if form.is_valid():
            messages.success(request, 'Account Updated')
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "is_vendor": CustomUser.objects.get(pk=request.user.pk).is_vendor #take the attribute Is_vendor of the custom user
            }
        )
    context['account_form'] = form
    return render(request, 'registration/user_profile.html', context)
