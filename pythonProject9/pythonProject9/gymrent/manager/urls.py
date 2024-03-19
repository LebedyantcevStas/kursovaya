from django.urls import path
from .views import mainView, new_orders_view,shipping_orders_view, rent_orders_view,orderSingleView,postform3,postform4,postform5

app_name = 'manager'
urlpatterns = [
    path('manager', mainView.as_view(), name ='main'),
    path('manager/new_orders', new_orders_view.as_view(), name ='new_orders'),
    path('manager/rent_orders', rent_orders_view.as_view(), name ='rent_orders'),
    path('manager/shipping_orders', shipping_orders_view.as_view(), name ='shipping_orders'),
    path('manager/order/<int:id>/', orderSingleView.as_view(), name='order'),
    path("form3/", postform3),
    path("form4/", postform4),
    path("form5/", postform5)
]
