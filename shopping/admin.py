from django.contrib import admin

# Register your models here.
from .models import customer,category,product,cart,billing_details,order

admin.site.register(customer)
admin.site.register(category)
admin.site.register(product)
admin.site.register(cart)
admin.site.register(billing_details)
admin.site.register(order)