from django import forms
from .models import Order

class Meta:
    model = Order
    fields = [
        'orderId',
        'orderStartDate',
        'orderEndDate',
        'ownerUserId',
        'renterUserId',
        'productId'
    ]