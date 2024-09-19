from rest_framework.serializers import ModelSerializer
from .models import Customer, Provider, Auction


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class AuctionSerializer(ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'