from operations.binary_operations.BinaryOperation import BinaryOperation


class PowerOperation(BinaryOperation):
    """
    Represents the power operation in a calculator.
    extents BinaryOperation.
    """

    def priority(self) -> int:
        """
        Returns the priority level of the power operation.
        """
        return 3

    def perform(self, operand1: float, operand2: float) -> float:
        """
        Determines the power of two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        return: The power value of operand1 and operand2.
        """

        return operand1 ** operand2
