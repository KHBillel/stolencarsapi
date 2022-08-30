from django.shortcuts import render
from .serializers import VehiculeSerializer, Vehicule
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse

# Create your views here.


class VehiculeAPIViewDetail(APIView) :
    def get(self, request, pk) :
        try :
            vehicule = Vehicule.objects.get(pk=pk)
            return Response(VehiculeSerializer(vehicule, many=False).data)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
       

class VehiculeAPIViewDetailByMat(APIView) :
    def get(self, request, mat) :
        try :
            vehicule = Vehicule.objects.get(mat=mat)
            return Response(VehiculeSerializer(vehicule, many=False).data)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class VehiculeAPIViewList(APIView) :
    def get(self, request) :
        try :
            vehicules = Vehicule.objects.all()
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(VehiculeSerializer(vehicules, many=True).data)

    def post(self, request) :
        serializer = VehiculeSerializer(data=request.data)
        if serializer.is_valid(serializer) :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)