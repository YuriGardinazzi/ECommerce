from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Product


class SubmitButtonMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.id:
            self.helper.inputs[0].value = 'Update'
            self.helper.inputs[0].field_classes = 'btn btn-warning'
        else:
            self.helper.inputs[0].value = 'Create'
            self.helper.inputs[0].field_classes = 'btn btn-success'


class ProductCrispyForm(SubmitButtonMixin):

    helper = FormHelper()
    helper.form_id = 'product-crispy-form'
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = Product
        exclude = ('producer',)
