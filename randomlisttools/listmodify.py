from collections.abc import Iterable


def flatten_list(the_list):
    for i in the_list:
        if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
            yield from flatten_list(i)
        else:
            yield i


def remove_list_dupes(the_list):
    new_list = []
    for x in range(len(the_list)):
        if the_list[x] not in new_list:
            new_list.append(the_list[x])
    return new_list


def remove_list_dupes_inplace(the_list):
    x = 0
    while x < len(the_list):
        if the_list.count(the_list[x]) >= 2:
            for y in range(1, the_list.count(the_list[x])):
                the_list.remove(the_list[x])
            continue
        x += 1
    return the_list


def list_replace(the_list, replace_what, replace_with):
    """Replaces char with char for all values in a list.

    Args:
        the_list: The list on which to perform the replacement.
        replace_what: The char to replace
        replace_with: What to replace 'what' with.

    Returns:
        A list with the values replaced.
    """
    new_list = []
    for i in the_list:
        if isinstance(i, list):
            new_list.append(list_replace(i, replace_what, replace_with))
        elif isinstance(i, str):
            new_list.append(i.replace(replace_what, replace_with))
        else:
            new_list.append(i)

    return new_list
