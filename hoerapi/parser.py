from hoerapi.errors import MissingAttributeError, InvalidDataError


def parser_list(clazz, data):
    items = []

    if isinstance(data, list):
        for episode in data:
            try:
                items.append(clazz(episode))
            except KeyError as e:
                raise MissingAttributeError(e.args[0])
    else:
        raise InvalidDataError('not an array')

    return items


def parser_object(clazz, data):
    try:
        return clazz(data)
    except KeyError as e:
        raise MissingAttributeError(e)