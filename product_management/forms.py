from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Product





class ProductCrispyForm(forms.ModelForm):

    helper = FormHelper()
    helper.form_id = 'product-crispy-form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = Product
        exclude = ('producer',)
