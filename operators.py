"""
all the possible operators and their priority
"""
operators: dict = {'+': 1,  # plus

                   '-': 1,  # minus

                   '*': 2,  # multiplication

                   '/': 2,  # division

                   '^': 3,  # power

                   '%': 4,  # modulo

                   '@': 5,  # average

                   '$': 5,  # maximum

                   '&': 5,  # minimum

                   '~': 6,  # negative

                   '!': 6,  # factorial
                   }


def is_operator(op: str) -> bool:
    """
    check if op exists in the operations dict, returns true if exists else otherwise
    :param op: str of operand
    :return: true if exists else otherwise
    """
    return op in operators


def is_prior(op1: str, op2) -> bool:
    """
    returns weather op1 is prior to op2, based on the operations dict
    :param op1: str of operator
    :param op2: str of operator
    :return: true is op1 is prior to op2, else otherwise
    """
    if is_operator(op1) and is_operator(op2):
        return operators[op1] >= operators[op2]
    return False


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
