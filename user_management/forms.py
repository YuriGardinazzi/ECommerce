from PIL.Image import Image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CustomUser
from ecommerce import settings


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    is_vendor = forms.BooleanField(initial=False, required=False, label='Check if you\'re a vendor')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Choose your password wisely'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Choose your password wisely'}))

    helper = FormHelper()
    helper.form_id = 'Custom-User-Crispy-Form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'SignUp'))

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'is_vendor', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean(self):  # before the form does anything the method clean is run
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Credentials are wrong")


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'image', 'is_vendor')

    def __init__(self, *args, **kwargs):
        super(AccountUpdateForm, self).__init__(*args, **kwargs)
        #check if the instance exist
        if self.instance:
            if 'initial' in kwargs.keys():
                if kwargs['initial']['is_vendor']:
                    self.fields.pop('is_vendor')

    # check email not already in use
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
            except CustomUser.DoesNotExist:
                return email
            raise forms.ValidationError(f'Email {email} is already in use')

    # check username not already in use
    def clean_username(self):
        if self.is_valid():
            # check of the email
            username = self.cleaned_data['username']
            try:
                account = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
            except CustomUser.DoesNotExist:
                return username
            raise forms.ValidationError(f'Username {username} is already in use')

    def clean_name(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            return name

