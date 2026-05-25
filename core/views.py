from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import GymMemberDetails
from .serializers import HandlerSerializer
from .services import GymServiceLayer
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def membership_fee_api(request):
    if request.method == 'POST':
        serializer = HandlerSerializer(data=request.data)
        if serializer.is_valid():
            result = GymServiceLayer.process_membership_fee(serializer.data)
            print(result)
            print('In Repository Layer')
            return Response({"message" : "Data saved Sucessfully"},status=201)
        else:
            return Response({"error" : "Invalid Data"},status=400)