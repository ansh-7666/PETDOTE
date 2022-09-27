from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Details = models.TextField()
    Image = models.ImageField(upload_to='products')
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Available_quantity = models.IntegerField(default=0)
class order(models.Model):
    ID = models.AutoField(primary_key=True)
    Invoice_number = models.IntegerField(default=0)
    Date = models.DateField()
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)

class ordered_items(models.Model):
    ID = models.AutoField(primary_key=True)
    Order_ID = models.ForeignKey(order, on_delete=models.CASCADE)
    product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Total_price = models.IntegerField(default=0)
