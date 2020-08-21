from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm, AccountUpdateForm
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView


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
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "name": request.user.name,
            }
        )
    context['account_form'] = form
    return render(request, 'registration/user_profile.html', context)
