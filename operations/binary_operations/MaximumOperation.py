from operations.binary_operations.BinaryOperation import BinaryOperation


class MaximumOperation(BinaryOperation):
    """
    Represents a maximum operation in the calculator.
    extents BinaryOperation.
    """
    def priority(self) -> int:
        """
        Returns the priority of the maximum operation.
        """
        return 5

    def perform(self, operand1: float, operand2: float) -> float:
        """
        Determines the maximum of two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        :return: The maximum value of operand1 and operand2.
        """
        return max(operand1, operand2)
