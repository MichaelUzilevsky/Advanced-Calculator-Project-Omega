from operations.binary_operations.BinaryOperation import BinaryOperation


class SubtractionOperation(BinaryOperation):
    """
    Represents the subtraction operation in a calculator.
    extents BinaryOperation.
    """

    SUBTRACTION_PRIORITY = 1

    def __init__(self):
        super().__init__(priority=SubtractionOperation.SUBTRACTION_PRIORITY)

    def execute(self, operand1: float, operand2: float) -> float:
        """
        Determines the subtraction of two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        return: The subtraction value of operand1 and operand2.
        """
        return operand1 - operand2
