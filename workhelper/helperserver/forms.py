from django import forms
from .models import *


class Order_form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')


class Work_form(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('description', 'price')


class Spare_parts_form(forms.ModelForm):
    class Meta:
        model = Spare_parts
        fields = ('description', 'price')