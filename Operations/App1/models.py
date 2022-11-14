from django.db import models


class invent(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=500)
    buying_price=models.CharField(max_length=1000)
    qutity=models.FloatField(max_length=1000)
    selling_price=models.CharField(max_length=1000)

class billing(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=500)
    customer_name = models.CharField(max_length=1000)
    customer_mobile = models.CharField(max_length=1000)
    selling_price = models.CharField(max_length=1000)
    buying_price = models.CharField(max_length=1000)
    amount = models.CharField(max_length=1000)
    discount = models.CharField(max_length=1000)
    total = models.CharField(max_length=1000)