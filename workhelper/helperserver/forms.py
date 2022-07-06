from django import forms
from .models import *


class Order_form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')