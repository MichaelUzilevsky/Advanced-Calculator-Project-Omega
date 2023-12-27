from operators import is_operator, is_prior


def to_postfix(infix: list[str]) -> list[str]:
    """
    receives a list of chars in infix way of writing and converts this list to postfix list and then returns it
    :param infix: (list) of chars representing each operator or operand in the infix expression, it is assumed that
    this is correct and there are no errors in the expression
    :return: (list) returns the postfix expression for the given infix expression
    """
    postfix: list[str] = []
    operators_stack: list[str] = []
    for item in infix:
        if item.isdigit():
            postfix.append(item)

        elif item == '(':
            operators_stack.append(item)

        elif item == ')':
            while operators_stack and operators_stack[-1] != '(':
                postfix.append(operators_stack.pop())

            operators_stack.pop()  # remove '(' from the stack

        elif is_operator(item):
            if operators_stack and operators_stack[-1] == '(':
                operators_stack.append(item)

            else:
                while operators_stack and is_prior(operators_stack[-1], item):
                    postfix.append(operators_stack.pop())

                operators_stack.append(item)

    while operators_stack:
        postfix.append(operators_stack.pop())

    return postfix


if __name__ == '__main__':
    print(to_postfix(["(", "2", "+", "3", "!", ")", "*", "4"]))  # result ['2', '3', '!', '+', '4', '*']


