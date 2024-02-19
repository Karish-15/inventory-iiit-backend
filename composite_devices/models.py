from django.db import models

class CompositeDevices(models.Model):
    class DeviceChoices(models.TextChoices):
        DESKTOP = 'desktop', 'Desktop'
        MICROCONTROLLER = 'microcontroller', 'Microcontroller'
        TEST_DEVICE = 'test_device', 'Test Device'
    class WarrantyChoices(models.TextChoices):
        STOCK = 'stock', 'Stock'
        EXTENDED = 'extended', 'Extended'
        AMC = 'amc', 'AMC'
    id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100, choices=DeviceChoices.choices)
    building = models.CharField(max_length=100)
    building_block = models.CharField(max_length=100)
    building_floor = models.IntegerField()
    specifications = models.TextField()
    oem_name = models.TextField()
    vendor = models.TextField()
    purchase_date = models.DateField()
    warranty_type = models.CharField(max_length=100, choices=WarrantyChoices.choices)

    def __str__(self):
        return self.name + ' [' + self.serial_number + ']'



