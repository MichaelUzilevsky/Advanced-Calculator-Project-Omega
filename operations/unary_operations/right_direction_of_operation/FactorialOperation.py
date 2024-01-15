from operations.unary_operations.right_direction_of_operation.RightUnaryOperation import RightUnaryOperation


class FactorialOperation(RightUnaryOperation):
    """
    Represents the factorial operation in a calculator.
    extends RightUnaryOperation.
    """
    def priority(self) -> int:
        """
        Returns the priority level of the factorial operation.
        """
        return 6

    def perform(self, operand: int) -> int:
        """
        Calculates the factorial of the provided integer operand.
        :param operand: The operand as an integer.
        :return: The factorial of the operand.
        :raises ValueError: If the operand is not an integer or is less than 0.
        """
        """
        returns the factorial of operand
        :param operand: (int)
        :return: operand!
        :raise ValueError if operand is not valid for factorial operation
        """
        if int(operand) != operand or operand < 0:
            raise ValueError(f"{operand} must be an integer and non-negative to calculate factorial.")
        if operand == 0:
            return 1
        result: int = 1
        for i in range(1, int(operand) + 1):
            result *= i
        return result




