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


  def __str__(self):
      return self.name

class Discount(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  value = models.IntegerField()
  date_begin = models.DateTimeField()
  date_end = models.DateTimeField()


  def __str__(self):
      return f"{self.product.name}_{self.value}%_{self.date_end}"

class card_status(models.Model):
  # status_id = models.AutoField()
  status_name = models.CharField(max_length=100)


class stuff(models.Model):
  # stuff_id = models.AutoField()
  stuff_num = models.CharField(max_length=15)
  stuff_name = models.CharField(max_length=200)


class order_status(models.Model):
  # status_id = models.AutoField()
  status_num = models.CharField(max_length=200)

class order_gym(models.Model):
  order_date = models.DateTimeField()
  plan_return_date = models.DateTimeField()
  return_date = models.DateTimeField()
  status_int = models.ForeignKey(order_status, on_delete=models.CASCADE)
  forfeit = models.DecimalField(decimal_places=2, max_digits=8)
  deposit = models.DecimalField(decimal_places=2, max_digits=8)
  stuff = models.IntegerField()
  model_e=models.ManyToManyField(Product)