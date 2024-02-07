""" This is just a demo to show that serializers will also work the same """
from django import forms
from .models import Product

class ProductForm(forms.ModelFrom):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]