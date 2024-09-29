from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('cart/', CartDetailView.as_view(), name='cart_detail'),
    path('cart/add/<int:product_id>/', CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', CartRemoveView.as_view(), name='cart_remove'),
    path('cart/clear/', CartClearView.as_view(), name='cart_clear'),
]