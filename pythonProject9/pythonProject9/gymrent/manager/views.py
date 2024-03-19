from django.shortcuts import render
from django.views import View
from django.db.models import OuterRef, Subquery, F, ExpressionWrapper, DecimalField, Case, When, IntegerField
from django.utils import timezone
from django.http import HttpResponse
from django.db.models import Avg, Min, Max, Sum
from django.db import connection
from store.models import Order, order_gym_eqw
class mainView(View):

    def get(self, request):
        cursor=connection.cursor()
        cursor.execute("select count(o.id) as ord, sum(e.days*p.price) as money from public.store_order o join public.store_order_gym_eqw e on o.id=e.order_id join public.store_product p on e.product_id = p.id ")
        rows=cursor.fetchone()
        c=0
        m=0
        print(rows)
        c=rows[0]
        m=rows[1]

        return render(request, "manager/main.html", context={"money":m,"count":c})

class new_orders_view(View):

    def get(self, request):
        username = request.user.username
        rows=Order.objects.raw("SELECT o.id, contactphone, comment,date_order, date_shipping, time_shipping, adress,p.payment_name, s.status_name from public.store_order o join public.store_order_status s on s.id=o.status join public.store_payment p on p.id=o.pay_type where \"user\"=%s and o.status=1",[username])
        #with connection.cursor() as cursor:
            #cursor.execute("SELECT o.id, date_order, date_shipping, time_shipping, adress,p.payment_name, s.status_name from public.store_order o join public.store_order_status s on s.id=o.status join public.store_payment p on p.id=o.pay_type where \"user\"=%s",[username])
            #rows = cursor.fetchall()
        p=[]
        for i in rows:
            p.append(i)
        return render(request, "manager/new_orders.html", context={"data": p })



class rent_orders_view(View):

    def get(self, request):
        username = request.user.username
        rows=Order.objects.raw("SELECT o.id, contactphone, comment,date_order, date_shipping, time_shipping, adress,p.payment_name, s.status_name from public.store_order o join public.store_order_status s on s.id=o.status join public.store_payment p on p.id=o.pay_type where \"user\"=%s and o.status=4",[username])
        #with connection.cursor() as cursor:
            #cursor.execute("SELECT o.id, date_order, date_shipping, time_shipping, adress,p.payment_name, s.status_name from public.store_order o join public.store_order_status s on s.id=o.status join public.store_payment p on p.id=o.pay_type where \"user\"=%s",[username])
            #rows = cursor.fetchall()
        p=[]
        for i in rows:
            p.append(i)
        return render(request, "manager/rent_orders.html", context={"data": p })



class shipping_orders_view(View):

    def get(self, request):
        username = request.user.username
        rows=Order.objects.raw("SELECT o.id, contactphone, comment,date_order, date_shipping, time_shipping, adress,p.payment_name, s.status_name from public.store_order o join public.store_order_status s on s.id=o.status join public.store_payment p on p.id=o.pay_type where \"user\"=%s and o.status=2",[username])
        #with connection.cursor() as cursor:
            #cursor.execute("SELECT o.id, date_order, date_shipping, time_shipping, adress,p.payment_name, s.status_name from public.store_order o join public.store_order_status s on s.id=o.status join public.store_payment p on p.id=o.pay_type where \"user\"=%s",[username])
            #rows = cursor.fetchall()
        p=[]
        for i in rows:
            p.append(i)
        return render(request, "manager/shipping_orders.html", context={"data": p })

class orderSingleView(View):

    def get(self, request, id):
        data = order_gym_eqw.objects.all()
        data = data.filter(order=id)
        data=order_gym_eqw.objects.raw("select o.id,sp.name , sp.price , o.days, ord.status  from public.store_order_gym_eqw o join public.store_product sp on o.product_id =sp.id  join public.store_order ord on ord.id=o.order_id where o.order_id =%s",[id])
        #with connection.cursor() as cursor:
            #cursor.execute("select o.id,sp.name , sp.price , o.days  from public.store_order_gym_eqw o join public.store_product sp on o.product_id =sp.id  where o.order_id =%s",[id])
            #data = cursor.fetchall()
        sp = []
        total = 0
        status=0
        for i in data:
            sp.append(i)
            total += i.price * i.days
            status=i.status
        status1 = 0
        status2 = 0
        status3 = 0
        if status==1:
            status1=1
        if status == 2:
            status2 = 1
        if status == 4:
            status3 = 1
        return render(request, "manager/order.html", context={"data": sp, "id": id, "total": total, "status1": status1,"status2": status2,"status3": status3})

def postform3(request):
    order = request.POST.get("id", 1)
    s = Order.objects.get(id=order)
    s.status=2
    s.save()
    return HttpResponse("<h1>Заказ передан в доставку</h1><a href='http://127.0.0.1:8000/manager/new_orders'><p>назад</p></a>")


def postform4(request):
    order = request.POST.get("id", 1)
    s = Order.objects.get(id=order)
    s.status=4
    s.save()
    return HttpResponse("<h1>Заказ доставлен</h1><a href='http://127.0.0.1:8000/manager/new_orders'><p>назад</p></a>")


def postform5(request):
    order = request.POST.get("id", 1)
    s = Order.objects.get(id=order)
    s.status=5
    s.save()
    return HttpResponse("<h1>Заказ возвращен</h1><a href='http://127.0.0.1:8000/manager/new_orders'><p>назад</p></a>")

