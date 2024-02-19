from rest_framework import serializers

from .models import CompositeDevices

class CompositeDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompositeDevices
        fields = '__all__'