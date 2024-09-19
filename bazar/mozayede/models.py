from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)

class Provider(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)

class Auction(models.Model):
    start_price =models.IntegerField(default=0)
    current_price =models.IntegerField(default=start_price ,blank=True,null=True)
    mahsool = models.CharField(max_length=15)
    start_date = models.TimeField(auto_now_add=True)
    end_date = models.TimeField(blank=True , null= True)
    provider = models.ForeignKey(Provider , on_delete=models.CASCADE ,related_name="prov")
    last_customer = models.ForeignKey(Customer , on_delete=models.CASCADE ,related_name="cust")


