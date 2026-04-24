from django.urls import path
from core import views

urlpatterns = [
    path('response/',views.home,name='home'),
    path('login/',views.login,name='login')
]
