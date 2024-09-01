from pprint import pprint
def introspection_info(obj):
    info = {}
    # Получаем тип объекта
    info['type'] = type(obj).__name__

    # Получаем атрибуты объекта
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    # Получаем методы объекта

    info['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]

    info['module'] = getattr(obj.__class__, '__module__', None)

    return info


number_info = introspection_info(42)
pprint(number_info)