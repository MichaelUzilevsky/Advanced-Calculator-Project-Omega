from operators import is_float
from postfix_convertor import to_postfix


def solve_postfix(postfix: list[str]) -> float:
    """
    this function receives a postfix expression and returns its solution
    :param postfix: list[str] that represent valid postfix expression
    :return: the solution of this expression
    :raise ZeroDivisionError if there is a division by 0
    :raise ValueError if there is an attempt to factorial negative or float number
    """
    solution_stack = []
    for item in postfix:
        if is_float(item):
            solution_stack.append(float(item))

        else:
            num2 = solution_stack.pop()
            num1 = 0
            # if unary operator only one operator is needed
            if item not in "~!":
                num1 = solution_stack.pop()

            match item:
                case '+':
                    solution_stack.append(add(num1, num2))
                case '-':
                    solution_stack.append(subtract(num1, num2))
                case '*':
                    solution_stack.append(multiply(num1, num2))
                case '/':
                    solution_stack.append(divide(num1, num2))
                case '^':
                    solution_stack.append(power(num1, num2))
                case '%':
                    solution_stack.append(modulo(num1, num2))
                case '@':
                    solution_stack.append(average(num1, num2))
                case '$':
                    solution_stack.append(maximum(num1, num2))
                case '&':
                    solution_stack.append(minimum(num1, num2))
                case '~':
                    solution_stack.append(negative(num2))
                case '!':
                    solution_stack.append(factorial(num2))

                case _:
                    print("Unknown operator")

    return solution_stack.pop()


def add(a: float, b: float) -> float:
    """
    sums a and b and returns it
    :param a: (float)
    :param b: (float)
    :return: a + b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    subtracts b from a and returns it
    :param a: (float)
    :param b: (float)
    :return: a - b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    multiplies a by b and returns it
    :param a: (float)
    :param b: (float)
    :return: a * b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    divided b from a and returns it
    :param a: (float)
    :param b: (float)
    :return: a / b
    :raise ZeroDivisionError if b is zero
    """
    if b != 0:
        return a / b
    raise ZeroDivisionError


def power(a: float, b: float) -> float:
    """
    powers a by b, and returns it
    :param a: (float)
    :param b: (float)
    :return: a^b
    """
    return a ** b


def modulo(a: float, b: float) -> float:
    """
    returns the modulo of a divided by b
    :param a: (float)
    :param b: (float)
    :return: a % b
    """
    return a % b


def average(a: float, b: float) -> float:
    """
    returns the average of a and b
    :param a: (float)
    :param b: (float)
    :return: (a + b) / 2
    """
    return (a + b) / 2


def maximum(a: float, b: float) -> float:
    """
    returns the max of a and b
    :param a: (float)
    :param b: (float)
    :return: max(a, b)
    """
    return max(a, b)


def minimum(a: float, b: float) -> float:
    """
    returns the min of a and b
    :param a: (float)
    :param b: (float)
    :return: min(a, b)
    """
    return min(a, b)


def negative(a: float) -> float:
    """
    returns the negative of a
    :param a: (float)
    :return: 0 - a
    """
    return -a


def factorial(a: int) -> int:
    """
    returns the factorial of a
    :param a: (int)
    :return: a!
    :raise Value error if a is not valid for factorial operation
    """
    if int(a) != a or a < 0:
        raise ValueError(f"{a} must be an int, and above 0")
    if a == 0:
        return 1
    result: int = 1
    for i in range(1, int(a) + 1):
        result *= i
    return result


if __name__ == '__main__':
    print(solve_postfix(to_postfix(['(', '10', '@', '12', '/', '4', '/', '2', ')', '!'])))

