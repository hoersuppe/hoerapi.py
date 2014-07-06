from hoerapi.errors import MissingAttributeError, InvalidDataError


def parser_list(clazz, data):
    if isinstance(data, list):
        return [parser_object(clazz, item) for item in data]
    elif data is None:
        return []
    else:
        raise InvalidDataError('not an array')


def parser_object(clazz, data):
    try:
        return clazz(data)
    except KeyError as e:
        raise MissingAttributeError(e)