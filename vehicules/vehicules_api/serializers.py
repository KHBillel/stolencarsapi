from .models import Vehicule
from rest_framework import serializers


class VehiculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicule
        fields = ['nc', 'mat', 'vbrand', 'vmodel', 'isStolen', 'short_description']

