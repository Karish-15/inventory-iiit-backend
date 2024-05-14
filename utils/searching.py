from django.db.models import Q

from resources.models import SW_Resources, Computing_Resources, IO_Resources, NW_Resources
from resources.serializers import SW_ResourcesSerializer, Computing_ResourcesSerializer, IO_ResourcesSerializer, NW_ResourcesSerializer

def search_resource(filters, resource_type: str = None):
    """
        Resource type: [sw, computing, io, nw]
    """
    fields = ['model', 'serial_number', 'building', 'building_block', 'building_floor']
    Qr = None
    for field in fields:
        if field in filters:
            q = Q(**{"%s__contains" % field: filters.get(field, "") })
            Qr = Qr & q if Qr else q

    SW_results = SW_Resources.objects.all().filter(Qr)
    Computing_results = Computing_Resources.objects.all().filter(Qr)
    IO_results = IO_Resources.objects.all().filter(Qr)
    NW_results = NW_Resources.objects.all().filter(Qr)

    SW_serializer = SW_ResourcesSerializer(SW_results, many=True)
    Computing_serializer = Computing_ResourcesSerializer(Computing_results, many=True)
    IO_serializer = IO_ResourcesSerializer(IO_results, many=True)
    NW_serializer = NW_ResourcesSerializer(NW_results, many=True)

    response = {
        "total": len(SW_serializer.data) + len(Computing_serializer.data) + len(IO_serializer.data) + len(NW_serializer.data),
        "sw_data": SW_serializer.data,
        "computing_data": Computing_serializer.data,
        "io_data": IO_serializer.data,
        "nw_data": NW_serializer.data,
    }

    resource_type = resource_type + "_data" if resource_type is not None else None
    if resource_type is not None:
        response = {
            resource_type: response[resource_type],
            "total": len(response[resource_type])
        }

    return response