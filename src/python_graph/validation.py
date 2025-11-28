def _check_is_string(value: str):
    return True, f'"{value}"'


def _check_is_int(value: str):
    if not value.isdigit():
        return False, None
    return True, int(value)


def _check_is_float(value: str):
    if not value.replace('.', '', 1).isdigit():
        return False, None
    return True, float(value)


def _check_is_bool(value: str):
    lowered = value.lower()
    if lowered in ["true", "1", "yes"]:
        return True, "true"
    if lowered in ["false", "0", "no"]:
        return True, "false"
    return False, None

VALIDATORS = {
    str: _check_is_string,
    int: _check_is_int,
    float: _check_is_float,
    bool: _check_is_bool
}
