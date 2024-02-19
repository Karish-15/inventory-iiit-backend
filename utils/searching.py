from resources.models import SW_Resources, Computing_Resources, IO_Resources, NW_Resources

def search_resource(filters):
    SW_results = SW_Resources.objects.all().filter(**filters)
    Computing_results = Computing_Resources.objects.all().filter(**filters)
    IO_results = IO_Resources.objects.all().filter(**filters)
    NW_results = NW_Resources.objects.all().filter(**filters)

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

    return response