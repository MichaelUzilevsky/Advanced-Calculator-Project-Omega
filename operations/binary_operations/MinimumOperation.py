from operations.binary_operations.BinaryOperation import BinaryOperation


class MinimumOperation(BinaryOperation):
    """
    Represents a minimum operation in the calculator.
    extents BinaryOperation.
    """
    MINIMUM_PRIORITY = 5

    def __init__(self):
        super().__init__(priority=MinimumOperation.MINIMUM_PRIORITY)

    def execute(self, operand1: float, operand2: float) -> float:
        """
        Determines the minimum of two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        :return: The minimum value of operand1 and operand2.
        """
        return min(operand1, operand2)
