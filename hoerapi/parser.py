from hoerapi.errors import MissingAttributeError, InvalidDataError


def parser_list(clazz, data):
    items = []

    if isinstance(data, list):
        for item in data:
            items.append(parser_object(clazz, item))
    else:
        raise InvalidDataError('not an array')

    return items


def parser_object(clazz, data):
    try:
        return clazz(data)
    except KeyError as e:
        raise MissingAttributeError(e)