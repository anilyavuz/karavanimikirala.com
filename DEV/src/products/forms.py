from django import forms
from .models import Product
    
class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = [
                'productID',
                'productType',
                'productName',
                'productVerification',
                'productLicense',
                'user_id'
            ]


