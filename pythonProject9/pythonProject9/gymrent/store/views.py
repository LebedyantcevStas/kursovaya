from django.shortcuts import render
from django.views import View
from django.db.models import OuterRef, Subquery, F, ExpressionWrapper, DecimalField, Case, When, IntegerField
from django.utils import timezone
from .models import Product,Discount,  Cart, Order, order_gym_eqw
from django.http import HttpResponse
from datetime import datetime, date
from django.db.models import Avg, Min, Max, Sum
from django.db import connection
class ShopView(View):
    def get(self, request):
        # Создание запроса на получения всех действующих не нулевых скидок
        discount_value = Case(When(discount__value__gte=0,
                                   discount__date_begin__lte=timezone.now(),
                                   discount__date_end__gte=timezone.now(),
                                   then=F('discount__value')),
                              default=0,
                              output_field=DecimalField(max_digits=10, decimal_places=2)
                              )
        # Создание запроса на расчёт цены со скидкой
        price_with_discount = ExpressionWrapper(
            F('price') * (100.0 - F('discount_value')) / 100.0,
            output_field=IntegerField()
        )

        products = Product.objects.annotate(
            discount_value=discount_value,
            price_before=F('price'),
            price_after=price_with_discount
        ).values('id', 'name', 'image', 'price_before', 'price_after',
                 'discount_value')
        products=products.filter(amount__range = (1,10000))
        return render(request, 'store/shop.html', {"data": products, "all":"active","power":"", "velo":"","run":""})




class ShopView_run(View):
    def get(self, request):
        # Создание запроса на получения всех действующих не нулевых скидок
        discount_value = Case(When(discount__value__gte=0,
                                   discount__date_begin__lte=timezone.now(),
                                   discount__date_end__gte=timezone.now(),
                                   then=F('discount__value')),
                              default=0,
                              output_field=DecimalField(max_digits=10, decimal_places=2)
                              )
        # Создание запроса на расчёт цены со скидкой
        price_with_discount = ExpressionWrapper(
            F('price') * (100.0 - F('discount_value')) / 100.0,
            output_field=IntegerField()
        )

        products = Product.objects.annotate(
            discount_value=discount_value,

            price_before=F('price'),
            price_after=price_with_discount
        ).values('id', 'name', 'image', 'price_before', 'price_after',
                 'discount_value')
        products=products.filter(category=5)
        products = products.filter(amount__range = (1,10000))
        return render(request, 'store/shop.html', {"data": products, "all":"","power":"", "velo":"","run":"active"})




class ShopView_velo(View):
    def get(self, request):
        # Создание запроса на получения всех действующих не нулевых скидок
        discount_value = Case(When(discount__value__gte=0,
                                   discount__date_begin__lte=timezone.now(),
                                   discount__date_end__gte=timezone.now(),
                                   then=F('discount__value')),
                              default=0,
                              output_field=DecimalField(max_digits=10, decimal_places=2)
                              )
        # Создание запроса на расчёт цены со скидкой
        price_with_discount = ExpressionWrapper(
            F('price') * (100.0 - F('discount_value')) / 100.0,
            output_field=IntegerField()
        )

        products = Product.objects.annotate(
            discount_value=discount_value,

            price_before=F('price'),
            price_after=price_with_discount
        ).values('id', 'name', 'image', 'price_before', 'price_after',
                 'discount_value')
        products=products.filter(category=2)
        products = products.filter(amount__range = (1,10000))
        return render(request, 'store/shop.html', {"data": products, "all":"","power":"", "velo":"active","run":""})




class ShopView_power(View):
    def get(self, request):
        # Создание запроса на получения всех действующих не нулевых скидок
        discount_value = Case(When(discount__value__gte=0,
                                   discount__date_begin__lte=timezone.now(),
                                   discount__date_end__gte=timezone.now(),
                                   then=F('discount__value')),
                              default=0,
                              output_field=DecimalField(max_digits=10, decimal_places=2)
                              )
        # Создание запроса на расчёт цены со скидкой
        price_with_discount = ExpressionWrapper(
            F('price') * (100.0 - F('discount_value')) / 100.0,
            output_field=IntegerField()
        )

        products = Product.objects.annotate(
            discount_value=discount_value,

            price_before=F('price'),
            price_after=price_with_discount
        ).values('id', 'name', 'image', 'price_before', 'price_after',
                 'discount_value')
        products=products.filter(category=3)
        products = products.filter(amount__range = (1,10000))
        return render(request, 'store/shop.html', {"data": products,"all":"","power":"active", "velo":"","run":""})










class CartView(View):

    def get(self, request):
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        data = Cart.objects.all()
        data=data.filter(user=username)
        sp = []
        total=0
        for i in data:
            sp.append(i)
            total+=i.product.price
        return render(request, "store/cart.html", context={"data":sp, "total":total})


class ProductSingleView(View):

    def get(self, request, id):
        data = Product.objects.get(id=id)
        return render(request,
                      "store/product-single.html",
                      context={'name': data.name,
                               'description': data.description,
                               'price': data.price,
                               'rating': 5.0,
                               'url': data.image.url,
                               'id':id
                               })


class AboutView(View):

    def get(self, request):
        return render(request, 'store/about.html')



def postform(request):
    fcs2 = request.POST.get("id", 1)
    s = Cart(user=request.user.username, product_id=fcs2)
    s.save()
    return HttpResponse("<h1>товар добавлен</h1><a href='http://127.0.0.1:8000/'><p>назад</p></a>")




def postform_order(request):
    adr = request.POST.get("adress", 1)
    com = request.POST.get("comment", 1)
    date_shipping = request.POST.get("date_shipping", 1)
    time_shipping = request.POST.get("select", 1)
    pay_type= request.POST.get("select2", 1)
    phone=request.POST.get("phone", 1)
    date_return=request.POST.get("date_return", 1)


    user1=request.user.username

    s = Order(user=request.user.username, date_order=datetime.now(), adress=adr, comment=com,date_shipping=date_shipping,time_shipping=time_shipping, status=1,contactphone=phone, pay_type= pay_type, date_return=date_return)
    s.save()

    max_id = Order.objects.aggregate(Max("id"))
    with connection.cursor() as cursor:
        cursor.execute("update public.store_product set amount=amount-1 where id in (select product_id from public.store_cart where \"user\"=%s)", [request.user.username])
    with connection.cursor() as cursor:
        cursor.execute("insert into public.store_order_gym_eqw(days, order_id, product_id) select (select date_return-date_shipping from public.store_order order by id desc limit 1), (select max(id) from public.store_order), product_id from public.store_cart where \"user\"=%s", [request.user.username])
    with connection.cursor() as cursor:
        cursor.execute("delete from public.store_cart where \"user\"=%s", [request.user.username])




    return HttpResponse("<h1>товар добавлен</h1><a href='http://127.0.0.1:8000/'><p>назад</p></a>")



class OrdersView(View):

    def get(self, request):
        username = request.user.username
        rows=Order.objects.raw("SELECT o.id, date_order, date_return, date_shipping, time_shipping, adress,p.payment_name, s.status_name from public.store_order o join public.store_order_status s on s.id=o.status join public.store_payment p on p.id=o.pay_type where \"user\"=%s",[username])
        #with connection.cursor() as cursor:
            #cursor.execute("SELECT o.id, date_order, date_shipping, time_shipping, adress,p.payment_name, s.status_name from public.store_order o join public.store_order_status s on s.id=o.status join public.store_payment p on p.id=o.pay_type where \"user\"=%s",[username])
            #rows = cursor.fetchall()
        p=[]
        for i in rows:
            p.append(i)
        return render(request, "store/orders.html", context={"data": p })

class orderSingleView(View):

    def get(self, request,id):
        data = order_gym_eqw.objects.all()
        data = data.filter(order=id)
        sp = []
        total = 0
        for i in data:
            sp.append(i)
            total += i.product.price * i.days
        return render(request, "store/order.html", context={"data": sp, "id":id, "total":total})






