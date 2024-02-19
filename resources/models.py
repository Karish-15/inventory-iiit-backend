from django.db import models
from django.urls import reverse

from composite_devices.models import CompositeDevices

class SW_Resources(models.Model):
    class WarrantyChoices(models.TextChoices):
        STOCK = 'stock', 'Stock'
        EXTENDED = 'extended', 'Extended'
        AMC = 'amc', 'AMC'
    product_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    building_block = models.CharField(max_length=100)
    building_floor = models.IntegerField()
    make = models.TextField()
    model = models.TextField()
    specifications = models.TextField()
    oem_name = models.TextField()
    vendor = models.TextField()
    purchase_date = models.DateField()
    warranty_type = models.CharField(max_length=100, choices=WarrantyChoices.choices)
    attached_device = models.ForeignKey(CompositeDevices, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type + ' [' + self.product_type + '-' + self.serial_number + ']'

    def get_absolute_url(self):
        return reverse('sw_resources_detail', args=[str(self.product_id)])

class Computing_Resources(models.Model):
    class WarrantyChoices(models.TextChoices):
        STOCK = 'stock', 'Stock'
        EXTENDED = 'extended', 'Extended'
        AMC = 'amc', 'AMC'
    product_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    building_block = models.CharField(max_length=100)
    building_floor = models.IntegerField()
    make = models.TextField()
    model = models.TextField()
    specifications = models.TextField()
    oem_name = models.TextField()
    vendor = models.TextField()
    purchase_date = models.DateField()
    warranty_type = models.CharField(max_length=100, choices=WarrantyChoices.choices)
    attached_device = models.ForeignKey(CompositeDevices, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type + ' [' + self.product_type + '-' + self.serial_number + ']'

    def get_absolute_url(self):
        return reverse('computing_resources_detail', args=[str(self.product_id)])

class IO_Resources(models.Model):
    class WarrantyChoices(models.TextChoices):
        STOCK = 'stock', 'Stock'
        EXTENDED = 'extended', 'Extended'
        AMC = 'amc', 'AMC'
    product_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    building_block = models.CharField(max_length=100)
    building_floor = models.IntegerField()
    make = models.TextField()
    model = models.TextField()
    specifications = models.TextField()
    oem_name = models.TextField()
    vendor = models.TextField()
    purchase_date = models.DateField()
    warranty_type = models.CharField(max_length=100, choices=WarrantyChoices.choices)
    attached_device = models.ForeignKey(CompositeDevices, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type + ' [' + self.product_type + '-' + self.serial_number + ']'

    def get_absolute_url(self):
        return reverse('io_resources_detail', args=[str(self.product_id)])

class NW_Resources(models.Model):
    class WarrantyChoices(models.TextChoices):
        STOCK = 'stock', 'Stock'
        EXTENDED = 'extended', 'Extended'
        AMC = 'amc', 'AMC'
    product_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    building_block = models.CharField(max_length=100)
    building_floor = models.IntegerField()
    make = models.TextField()
    model = models.TextField()
    specifications = models.TextField()
    oem_name = models.TextField()
    vendor = models.TextField()
    purchase_date = models.DateField()
    warranty_type = models.CharField(max_length=100, choices=WarrantyChoices.choices)
    attached_device = models.ForeignKey(CompositeDevices, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.type + ' [' + self.product_type + '-' + self.serial_number + ']'

    def get_absolute_url(self):
        return reverse('nw_resources_detail', args=[str(self.product_id)])






