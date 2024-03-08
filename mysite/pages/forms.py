
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'books', 'total_price']

    def clean_total_price(self):
        total_price = self.cleaned_data['total_price']
        # Add your validation logic here if needed
        return total_price
