from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelChoiceField

from .models import Product, MyCategory


# Personalized field that show just the name of the object Category
class CategoryChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return '{name}'.format(name=obj.name)


class ProductCrispyForm(forms.ModelForm):
    category = CategoryChoiceField(queryset=MyCategory.objects.all())

    helper = FormHelper()
    helper.form_id = 'product-crispy-form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = Product
        exclude = ('producer',)
