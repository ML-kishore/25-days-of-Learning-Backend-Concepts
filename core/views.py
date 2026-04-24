from django.shortcuts import render
from django.http import HttpResponse
import time



# Create your views here.
def home(request):
    print("Auth passed ........✅✅✅✅")
    print("Inside view (Processing)")
    print(f"Data : {request.custom_data}")
    return HttpResponse("<h1>Done.....</h1>")


def login(request):
    print("Logged in .... dummyfull 😂😂😂")
    return HttpResponse("<h1>Logged in Successfully . . . . . </h1>")
