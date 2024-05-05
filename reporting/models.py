import uuid
from datetime import datetime

from django.db import models

from django.conf import settings
from utils.searching import search_resource
from utils.constants import SEARCH_MODEL_MAPPING

class Reports(models.Model):
    report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serial_number = models.CharField(max_length=100)
    # product_table: sw, computing, io, nw
    product_table = models.CharField(max_length=100, null = True)
    stage = models.IntegerField(default=1)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    product_url = models.CharField(max_length=100, null = True)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.serial_number + ' [' + self.product_table + ']'

    def save(self, *args, **kwargs):
        filters = {
            'serial_number': self.serial_number
        }
        response = search_resource(filters)
        for key, value in response.items():
            if key in ['sw_data', 'computing_data', 'io_data', 'nw_data'] and len(value)>0:
                self.product_table = SEARCH_MODEL_MAPPING[key].__name__
        super().save(*args, **kwargs)

class UnderRepair(models.Model):
    report_id = models.ForeignKey(Reports, on_delete=models.CASCADE)
    expected_return_date = models.DateTimeField()
    repairing_company = models.CharField(max_length=100)
    under_repair = models.BooleanField(default=True)
    

