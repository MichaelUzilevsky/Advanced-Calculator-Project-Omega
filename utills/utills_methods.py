def is_float(string):
    """
    checks if a given string is float, returns ture if it is, else returns false. in case of error false is returned
    :param string:
    :return: bool, true -> float, false not float or int
    """
    try:
        float(string)
        return True
    except ValueError:
        return False
