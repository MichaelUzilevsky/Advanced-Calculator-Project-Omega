from operations.unary_operations.right_direction_of_operation.RightUnaryOperation import RightUnaryOperation


class FactorialOperation(RightUnaryOperation):
    def priority(self) -> int:
        return 6

    def perform(self, operand: int) -> int:
        """
        returns the factorial of operand
        :param operand: (int)
        :return: operand!
        :raise ValueError if operand is not valid for factorial operation
        """
        if int(operand) != operand or operand < 0:
            raise ValueError(f"{operand} must be an int, and above 0. to do {operand}!")
        if operand == 0:
            return 1
        result: int = 1
        for i in range(1, int(operand) + 1):
            result *= i
        return result




