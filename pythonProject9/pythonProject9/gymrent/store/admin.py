from .models import Product, Category,Discount, order_status, payment
from django.contrib import admin


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(order_status)
admin.site.register(payment)