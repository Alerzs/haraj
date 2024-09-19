from .views import *
from django.urls import path

urlpatterns = [
    path('new-auction/', NewAuction.as_view()),
    path('add-offer/', AddOffer.as_view()),
]