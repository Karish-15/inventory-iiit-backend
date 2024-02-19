from rest_framework import serializers

from .models import Reports
from utils.searching import search_resource
from utils.constants import SEARCH_MODEL_MAPPING

class ReportsSerializer(serializers.ModelSerializer):
    resource_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Reports
        fields = '__all__'

    def get_resource_url(self, obj):
        filters = {
            'serial_number': obj.serial_number
        }
        response = search_resource(filters)
        for key, value in response.items():
            if key in ['sw_data', 'computing_data', 'io_data', 'nw_data'] and len(value)>0:
                resource_model = SEARCH_MODEL_MAPPING[key](**value[0])
                return resource_model.get_absolute_url()

        return None