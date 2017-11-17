from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder

from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('login', 'Login', css_class='btn-primary')
            )
        )


class NewProductForm(forms.Form):
    barcode= forms.CharField(label="Código de barras",
            max_length=32,
            required=True
            )
    name= forms.CharField(label="Nombre",
            max_length=140,
            required=True
            )

    def __init__(self, *args, **kwargs):
        super(NewProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()            
        self.helper.form_id = 'id-newProductForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.form_action = 'index'
        self.helper.add_input(Submit('submit', 'Enviar'))     

class NewReviewForm(forms.Form):
    title= forms.CharField(label="Título",
            max_length=50,
            required=True
            )
    text= forms.CharField(label="Texto",
            max_length=500,
            required=True
            )

    def __init__(self, *args, **kwargs):
        super(NewReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()            
        self.helper.form_id = 'id-newReviewForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
#        self.helper.form_action = 'product_detail'
        self.helper.add_input(Submit('submit', 'Enviar'))             


