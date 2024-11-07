import inspect


def introspection_info(obj):
    a = type(obj).__name__
    b = [a for a in dir(obj) if not a.startswith('__')]
    c = [a for a in dir(obj) if a.startswith('__')]
    d = introspection_info.__module__
    return {"type": a, "attributes": [b], 'methods': [c], 'module': d}


number_info = introspection_info(42)
print(number_info)
