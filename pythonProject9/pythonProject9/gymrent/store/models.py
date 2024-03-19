from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255)


  def __str__(self):
      return self.name


class Product(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  image = models.ImageField(upload_to='static/products/', null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  created_time = models.DateTimeField(auto_now_add=True)
  updated_time = models.DateTimeField(auto_now=True)
  amount = models.IntegerField(null=True)


  def __str__(self):
      return self.name

class Discount(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  value = models.IntegerField()
  date_begin = models.DateTimeField()
  date_end = models.DateTimeField()


  def __str__(self):
      return f"{self.product.name}_{self.value}%_{self.date_end}"



class order_status(models.Model):
  status_name = models.CharField(max_length=200)

class payment(models.Model):
 payment_name = models.CharField(max_length=200)


class Cart(models.Model):
  user=models.TextField()
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
  user=models.TextField(null=True)
  date_order = models.DateTimeField(null=True)
  date_shipping = models.DateField(null=True)
  time_shipping=models.TextField(null=True)
  status=models.IntegerField(null=True)
  contactphone = models.TextField(null=True)
  adress = models.TextField(null=True)
  comment = models.TextField(null=True)
  pay_type = models.IntegerField(null=True)
  date_return = models.DateField(null=True)


class order_gym_eqw(models.Model):
  order=models.ForeignKey(Order, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  days = models.IntegerField(default=0)

