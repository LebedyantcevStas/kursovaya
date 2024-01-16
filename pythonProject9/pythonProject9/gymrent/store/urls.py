from django.urls import path
from .views import ShopView, CartView, ProductSingleView, AboutView,ShopView_run,ShopView_velo, ShopView_power

app_name = 'store'
urlpatterns = [
    path('', ShopView.as_view(), name ='shop'),
    path('run/', ShopView_run.as_view(), name ='shop'),
    path('velo/', ShopView_velo.as_view(), name ='shop'),
    path('power/', ShopView_power.as_view(), name ='shop'),
    path('cart/', CartView.as_view(), name ='cart'),
    path('product/<int:id>/', ProductSingleView.as_view(), name = 'product'),
    path('about/', AboutView.as_view(), name='about')
]
