from operations.binary_operations.BinaryOperation import BinaryOperation


class ModuloOperation(BinaryOperation):
    """
    Represents the modulo operation in the calculator.
    extents BinaryOperation.
    """
    def priority(self) -> int:
        """
        Returns the priority level of the modulo operation.
        """
        return 4

    def perform(self, operand1: float, operand2: float) -> float:
        """
        Determines the reminder of two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        return: The reminder value of operand1 and operand2.
        """
        return operand1 % operand2
