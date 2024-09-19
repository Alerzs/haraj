from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User)

class Provider(models.Model):
    user = models.OneToOneField(User)

class Auction(models.Model):
    start_price =models.IntegerField()
    current_price =models.IntegerField(default=start_price ,blank=True,null=True)
    mahsool = models.CharField(max_length=15)
    provider = models.ForeignKey(Provider , on_delete=models.CASCADE ,related_name="prov")
    last_custoer = models.ForeignKey(Customer , on_delete=models.CASCADE ,related_name="cust")
    

