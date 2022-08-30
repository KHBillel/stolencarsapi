from .views import VehiculeAPIViewDetail, VehiculeAPIViewList, VehiculeAPIViewDetailByMat
from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import CoreJSONRenderer

urlpatterns = [
    path('vehicules/', VehiculeAPIViewList.as_view()),
    path('vehicule/nc/<str:pk>/', VehiculeAPIViewDetail.as_view()),
    path('vehicule/mat/<str:mat>/', VehiculeAPIViewDetailByMat.as_view()),
]
