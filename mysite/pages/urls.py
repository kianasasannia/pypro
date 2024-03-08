
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('order/create/', views.order_create, name='order_create'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]
