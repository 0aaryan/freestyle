from django.db import models

"""Declare models for YOUR_APP app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,default="", on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=20,null =  False,default="")
    address=models.CharField(max_length=20, null = False)
    pincode=models.IntegerField(null=False)
    phone_number=models.IntegerField(null=False)  
    def __str__(self):
        return self.customer_name

class category(models.Model):
    name=models.CharField(max_length=50, null = False)
    def __str__(self):
        return self.name

class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_category = models.ForeignKey(category, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=50, null = False)
    product_details = models.CharField(max_length=200, null = False,default="")
    product_price = models.IntegerField(null = False)
    image=models.ImageField(upload_to='productimages',default="")
    def __str__(self):
        return self.product_title

class cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null = False)
    def __str__(self):
        return str(self.cart_id)


class billing_details(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    billing_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, null = False)
    email=models.EmailField()
    address=models.CharField(max_length=250, null = False)
    state=models.CharField(max_length=20,null=False)
    city=models.CharField(max_length=20,null=False)
    pin=models.IntegerField(null=False)
    phone=models.IntegerField(null=False)
       

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    cart_id=models.ForeignKey(cart, on_delete=models.CASCADE)
    billing_detail=models.ForeignKey(billing_details, on_delete=models.CASCADE)
    order_date=models.DateField(auto_now_add=True)
    payment_status=models.BooleanField(default=False)
    shipping_initiated=models.BooleanField(default=False)
    shipped=models.BooleanField(default=False)

