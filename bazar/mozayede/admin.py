from django.contrib import admin
from .models import Customer, Provider, Auction

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    pass

