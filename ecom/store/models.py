from django.db import models
import datetime


class Category(models.Model):
    name= models.CharField(max_length=50)#
    def __str__(self):
        return self.name



class Product(models.Model):
    name= models.CharField(max_length= 50)
    price= models.DecimalField( decimal_places=2, max_digits=10)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    description= models.CharField(max_length=250, blank=True)
    image= models.ImageField(upload_to='uploads/product/')
    is_sale= models.BooleanField(default=False)
    sale_price= models.DecimalField(default=0, decimal_places=2, max_digits=6)
    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    phone= models.CharField(max_length=10)
    email= models.EmailField(max_length=100)
    password= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Order(models.Model):
    Customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    Product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    address= models.CharField(max_length=250)
    phone= models.CharField(max_length=10)
    date= models.DateField(datetime.date.today)
    status= models.BooleanField(default=False)
