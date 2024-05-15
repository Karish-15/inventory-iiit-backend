from rest_framework import serializers

from .models import Reports, UnderRepair
from utils.searching import search_resource
from utils.constants import SEARCH_MODEL_MAPPING

class ReportsSerializer(serializers.ModelSerializer):
    resource_url = serializers.SerializerMethodField()
    expected_return_date = serializers.SerializerMethodField()
    reparing_company = serializers.SerializerMethodField()

    class Meta:
        model = Reports
        fields = '__all__'

    def get_resource_url(self, obj: Reports):
        filters = {
            'serial_number': obj.serial_number,
        }
        response = search_resource(filters)
        for key, value in response.items():
            if key in ['sw_data', 'computing_data', 'io_data', 'nw_data'] and len(value)>0:
                value[0]['supervisor'] = obj.created_by
                resource_model = SEARCH_MODEL_MAPPING[key](**value[0])
                return resource_model.get_absolute_url()

        return None
    
    def get_expected_return_date(self, obj: Reports):
        report_id = obj.report_id
        try:
            under_repair_report = UnderRepair.objects.get(report_id=report_id)
            return under_repair_report.expected_return_date
        except Exception:
            return None
        
    def get_reparing_company(self, obj: Reports):
        report_id = obj.report_id
        try:
            under_repair_report = UnderRepair.objects.get(report_id=report_id)
            return under_repair_report.repairing_company
        except Exception:
            return None