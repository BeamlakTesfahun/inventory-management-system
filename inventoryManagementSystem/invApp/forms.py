from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'name': forms.TextInput(
                attrs={'placeholder':'e.g. jeans', 'class':'form-control'}),
            'sku': forms.TextInput(
                attrs={'placeholder':'e.g. JN56789', 'class':'form-control'}),
            'price': forms.NumberInput(
                attrs={'placeholder':'e.g. 49.99', 'class':'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'placeholder':'e.g. 25', 'class':'form-control'}),
            'supplier': forms.TextInput(
                attrs={'placeholder':'e.g. XYZ Ltd.', 'class':'form-control'}),
        }