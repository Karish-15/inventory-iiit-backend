from resources.models import SW_Resources, Computing_Resources, IO_Resources, NW_Resources

RESOURCE_TABLES = {
    'sw': 'SW_Resources',
    'computing': 'Computing_Resources',
    'io': 'IO_Resources',
    'nw': 'NW_Resources',
}

SEARCH_MODEL_MAPPING = {
    'sw_data': SW_Resources,
    'computing_data': Computing_Resources,
    'io_data': IO_Resources,
    'nw_data': NW_Resources,
}

