# In views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Order, OrderItem
from .forms import OrderForm

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return render(request, 'order_created.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'order_create.html', {'form': form})

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_detail.html', {'order': order})


