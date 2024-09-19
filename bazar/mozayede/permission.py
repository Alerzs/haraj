from rest_framework import permissions
from .models import Customer, Provider

class IsCustomer(permissions.BasePermission):
    if Customer.objects.filter(user=request.user).exists():
        return True
    else:
        return False
    
class IsProvider(permissions.BasePermission):
    if Provider.objects.filter(user=request.user).exists():
        return True
    else:
        return False

    



