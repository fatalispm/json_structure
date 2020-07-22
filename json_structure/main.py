from typing import Dict, List

basic_types = (bool, int, float, str, bytes)


def structure(dct: Dict):
    """
    Returns structure of the dct
    d = {'data': [{'age': 15, 'name': 'John'}]} should return
    {'data': List[{'age': int, name: str}]}
    :param dct: dict
    :return: dict
    """

    if not isinstance(dct, Dict):
        raise ValueError('dct should be Dict')

    result_dict = {}

    for key in dct:
        values = get_values(dct[key])
        result_dict[key] = values

    return result_dict


def get_values(value):
    if isinstance(value, basic_types):
        return type(value)

    if isinstance(value, Dict):
        return structure(value)

    if isinstance(value, List):
        types = set()
        possible_values = []

        for item in value:
            values = get_values(item)
            if str(values) not in types:
                types.add(str(values))
                possible_values.append(values)

        return possible_values

    return type(value)
