# Generated by Django 5.0.2 on 2024-02-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompositeDevices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('serial_number', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('device_type', models.CharField(choices=[('desktop', 'Desktop'), ('microcontroller', 'Microcontroller'), ('test_device', 'Test Device')], max_length=100)),
                ('building', models.CharField(max_length=100)),
                ('building_block', models.CharField(max_length=100)),
                ('building_floor', models.IntegerField()),
                ('specifications', models.TextField()),
                ('oem_name', models.TextField()),
                ('vendor', models.TextField()),
                ('purchase_date', models.DateField()),
                ('warranty_type', models.CharField(choices=[('stock', 'Stock'), ('extended', 'Extended'), ('amc', 'AMC')], max_length=100)),
            ],
        ),
    ]
