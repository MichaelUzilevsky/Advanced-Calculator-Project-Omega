from utills.utills_methods import is_float


class Parser:
    def __init__(self, operations):
        self.operations = operations  # A dictionary of operator and their symbols

    def is_operator(self, item):
        return item in self.operations

    def get_priority(self, operator: str) -> int:
        """
        :param operator: (str) representing the operator
        :return: the priority of the operator based on the operations dictionary
        """
        return self.operations[operator].priority()

    def to_postfix(self, infix: list[str]) -> list[str]:
        """
        receives a list of chars in infix way of writing and converts this list to postfix list and then returns it
        :param infix: (list) of chars representing each operator or operand in the infix expression, it is assumed that
        this is correct and there are no errors in the expression
        :return: (list) returns the postfix expression for the given infix expression
        """
        postfix: list[str] = []
        operators_stack: list[str] = []
        for item in infix:
            if is_float(item):
                postfix.append(item)

            elif item == '(':
                operators_stack.append(item)

            elif item == ')':
                while operators_stack and operators_stack[-1] != '(':
                    postfix.append(operators_stack.pop())

                operators_stack.pop()  # remove '(' from the stack

            elif self.is_operator(item):
                if operators_stack and operators_stack[-1] == '(':
                    operators_stack.append(item)

                else:
                    while operators_stack and operators_stack[-1] != "(" and self.get_priority(operators_stack[-1]) >= self.get_priority(item):
                        postfix.append(operators_stack.pop())

                    operators_stack.append(item)

        while operators_stack:
            postfix.append(operators_stack.pop())

        return postfix
