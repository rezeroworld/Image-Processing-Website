from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class Operation (forms.Form):
    imageURL = forms.CharField(label="URL de l'image ")
    operation = forms.CharField(label='Operation ')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.Form_method = 'post'

        self.helper.layout = Layout(
            'imageURL',
            'operation',
            Submit('submit', 'Submit', css_class='btn-success mt-3')
        )