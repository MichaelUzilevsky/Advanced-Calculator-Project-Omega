from operations.binary_operations.BinaryOperation import BinaryOperation


class DivisionOperation(BinaryOperation):
    """
    Represents a division operation in a calculator.
    extents BinaryOperation
    """

    def priority(self) -> int:
        """
        Returns the priority of the division operation.
        """
        return 2

    def perform(self, operand1: float, operand2: float) -> float:
        """
        Performs division on two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        :return: The result of dividing operand1 by operand2.
        :raises ZeroDivisionError: If operand2 is zero.
        """
        if operand2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return operand1 / operand2
