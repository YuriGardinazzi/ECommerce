from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db import models
from django import forms
from .models import Product
from user_management.models import CustomUser


# Create your models here.


class ProductCrispyForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_id = 'buy-product-crispy-form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = Product
        exclude = ('buyer','is_sent')
