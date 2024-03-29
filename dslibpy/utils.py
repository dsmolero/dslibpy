import sys


def insert_before(target_list, new_item, before_item):
    """
    Inserts item into target_list so that it comes before before_item if before_item is in target_list.
    The item is appended to target_list if before_item does not exist.
    """
    pos = target_list.index(before_item)
    if pos:
        target_list.insert(pos, new_item)
    else:
        target_list.append(new_item)
    return target_list


def remove_non_ascii_1(text):
    return ''.join(i for i in text if ord(i) < 128)


def str2bool(val):
    """
    Only the following strings will evaluate to True.
    'yes', 'true', 'yup', 'okay', 'ok', 'y', 'k', 't', '1'
    """
    if isinstance(val, str):
        string_values_for_true = ('yes', 'true', 'yup', 'okay', 'ok', 'y', 'k', 't', '1')
        return val.lower() in string_values_for_true
    else:
        return bool(val)


def eprint(*args, **kwargs):
    """
    Print to stderr
    """
    print(*args, file=sys.stderr, **kwargs)
