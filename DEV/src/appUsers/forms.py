from django import forms
from .models import AppUser

class AppUserForm(forms.ModelForm):
    
    class Meta:
        model = AppUser
        fields = [
            'appUserId',
            'email',
            'name',
            'lastName',
            'password',
            'productAmount',
            'rentedProductAmount'
        ]
        
