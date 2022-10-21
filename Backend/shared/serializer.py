def enum_serializer(type_enum):
    """
    This function should convert a list of tuples to a list of dictionaries
    """
    res = []
    for val in type_enum:
        res_val = {}
        res_val['value'] = val[0]
        res_val['label'] = val[1]
        res.append(res_val)
    
    return res