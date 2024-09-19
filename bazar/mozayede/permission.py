from rest_framework import permissions
from .models import Customer, Provider

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return Customer.objects.filter(user=request.user).exists()

class IsProvider(permissions.BasePermission):
    def has_permission(self, request, view):
        return Provider.objects.filter(user=request.user).exists()

    



