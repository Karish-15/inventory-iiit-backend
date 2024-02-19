from rest_framework import serializers

from . import models

class SW_ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SW_Resources
        fields = '__all__'

class Computing_ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Computing_Resources
        fields = '__all__'

class IO_ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IO_Resources
        fields = '__all__'

class NW_ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NW_Resources
        fields = '__all__'