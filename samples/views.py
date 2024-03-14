from django.shortcuts import render
from samples.serializers import CustomerComplaintsSerializer,ScheduledDirectorsSerializer,MobileInformationSerializer
from .models import CustomerComplaints,ScheduledDirectors,MobileInformation
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class CustomerComplaintsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerComplaints.objects.all()
    serializer_class = CustomerComplaintsSerializer


@api_view(['GET','PUT','PATCH','DELETE'])
def customer_details(request,id):
    try:
        CustomerComplaints_instance = CustomerComplaints.objects.get(pk=id)
    except CustomerComplaints.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CustomerComplaintsSerializer(CustomerComplaints_instance)
        return Response (serializer.data)
    
    elif request.method == 'PUT':
        serializer = CustomerComplaintsSerializer(CustomerComplaints_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = CustomerComplaintsSerializer(CustomerComplaints_instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        CustomerComplaints_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ScheduledDirectorsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScheduledDirectors.objects.all()
    serializer_class = ScheduledDirectorsSerializer


@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def director_details(request, id):
    try:
        ScheduledDirectors_instance = ScheduledDirectors.objects.get(pk=id)
    except ScheduledDirectors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ScheduledDirectorsSerializer(ScheduledDirectors_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ScheduledDirectorsSerializer(ScheduledDirectors_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ScheduledDirectorsSerializer(ScheduledDirectors_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ScheduledDirectors_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
class MobileInformationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MobileInformation.objects.all()
    serializer_class = MobileInformationSerializer
 
    
@api_view(['GET', 'PUT','PATCH', 'DELETE'])
def mobile_details(request, id):
    try:
        MobileInformation_instance = MobileInformation.objects.get(pk=id)
    except MobileInformation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MobileInformationSerializer(MobileInformation_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MobileInformationSerializer(MobileInformation_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = MobileInformationSerializer(MobileInformation_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        MobileInformation_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
