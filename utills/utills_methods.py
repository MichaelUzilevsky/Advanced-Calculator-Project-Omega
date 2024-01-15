from operations.OperationsFactory import OperationsFactory as Operators


def is_float(string: str) -> bool:
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


def is_open_parentheses(item: str) -> bool:
    """
    Returns true if the item received is open parentheses
    :param item: (str)
    :return: true if the item received is open parentheses, otherwise false
    """
    return item == "("


def is_close_parentheses(item: str) -> bool:
    """
    Returns true if the item received is open parentheses
    :param item: (str)
    :return: true if the item received is open parentheses, otherwise false
    """
    return item == ")"


def is_parentheses(item: str) -> bool:
    """
    Returns true if the item received is open parentheses
    :param item: (str)
    :return: true if the item received is open parentheses, otherwise false
    """
    return is_open_parentheses(item) or is_close_parentheses(item)


def is_operator(item: str) -> bool:
    """
    Returns whether an operator appears in the factory dictionary
    :param item:
    :return: is the item is a legal operator
    """
    return item in Operators.operations
