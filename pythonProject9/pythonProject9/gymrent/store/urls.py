from django.urls import path
from .views import ShopView, CartView, ProductSingleView, AboutView,ShopView_run,ShopView_velo, ShopView_power,OrdersView
from .views import postform, postform_order, orderSingleView

app_name = 'store'
urlpatterns = [
    path('', ShopView.as_view(), name ='shop'),
    path('run/', ShopView_run.as_view(), name ='shop'),
    path('velo/', ShopView_velo.as_view(), name ='shop'),
    path('power/', ShopView_power.as_view(), name ='shop'),
    path('cart/', CartView.as_view(), name ='cart'),
    path('product/<int:id>/', ProductSingleView.as_view(), name = 'product'),
    path('about/', AboutView.as_view(), name='about'),
    path("form1/", postform),
    path("form2/", postform_order),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('order/<int:id>/', orderSingleView.as_view(), name='order')
]
