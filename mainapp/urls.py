from django.urls import path
from django.contrib.auth.views import LogoutView

from . import admin
from .views import (
    BaseView,
    ProductDetailView,
    CategoryDetailView,
    CategoryGlobalDetailView,
    CartView,
    AddToCartView,
    DeleteFromCartView,
    ChangeQTYView,
    CheckoutView,
    MakeOrderView,
    LoginView,
    AboutView,
    RegistrationView,
)


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('/about', AboutView.as_view(), name='about'),
    path('products.category/products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category_global/<str:slug>/', CategoryGlobalDetailView.as_view(), name='category_global_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
