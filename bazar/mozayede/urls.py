from .views import *
from django.urls import path

urlpatterns = [
    path('new-auction/', NewAuction.as_view()),
    path('add-offer/<int:pk>', AddOffer.as_view()),
    path('login/',Login.as_view()),
]