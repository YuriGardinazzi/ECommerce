from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
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

