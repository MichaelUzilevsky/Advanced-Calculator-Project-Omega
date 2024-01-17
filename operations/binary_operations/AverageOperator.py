from operations.binary_operations.BinaryOperation import BinaryOperation


class AverageOperation(BinaryOperation):
    """
    Represents an Average operation in a calculator.
    extents BinaryOperation
    """
    AVERAGE_PRIORITY = 5

    def __init__(self):
        super().__init__(priority=AverageOperation.AVERAGE_PRIORITY)

    def execute(self, operand1: float, operand2: float) -> float:
        """
        Performs average on two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        :return: The result of the average of operand1 and operand2.
        """
        return (operand1 + operand2) / 2
