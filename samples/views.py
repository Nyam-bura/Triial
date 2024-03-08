from django.shortcuts import render
from samples.serializers import (CustomerComplaintsSerializer,ScheduledDirectorsSerializer,MobileInformationSerializer)
from .models import (CustomerComplaints,ScheduledDirectors,MobileInformation)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

class CustomerComplaintsApiView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = CustomerComplaints.objects.all().values()
    serializer_class = CustomerComplaintsSerializer
    permission_classes = [IsAuthenticated]  

    def formatted_date(self):
        return self.reporting_date.strftime("%d %B %Y")
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = CustomerComplaintsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerComplaintsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class AbstractModelApiView(GenericAPIView,ListModelMixin, CreateModelMixin):
#     queryset = AbstractModel.objects.all()
#     serializer_class = AbstractSerializer
#     permission_classes = [IsAuthenticated] 
    
#     def get(self, request):
#         queryset = self.get_queryset()
#         serializer = AbstractSerializer(queryset, many=True)
#         return Response(serializer.data)



class ScheduledDirectorsApiView(GenericAPIView,ListModelMixin, CreateModelMixin):
    queryset = ScheduledDirectors.objects.all()
    serializer_class = ScheduledDirectorsSerializer

    def get(self, request):
        queryset = self.get_queryset()
        serializer = ScheduledDirectorsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScheduledDirectorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MobileInformationApiView(GenericAPIView,ListModelMixin, CreateModelMixin):
    queryset = MobileInformation.objects.all()
    serializer_class = MobileInformationSerializer

    def get(self, request):
        queryset = self.get_queryset()
        serializer = MobileInformationSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MobileInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)