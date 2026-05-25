from django.urls import path,include
from . import views

urlpatterns = [
    path('checkout/',views.membership_fee_api,name='safe_checkout')
]


