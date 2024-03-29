from operations.binary_operations.BinaryOperation import BinaryOperation


class MultiplicationOperation(BinaryOperation):
    """
    Represents the multiplication operation in a calculator.
    extents BinaryOperation.
    """
    MULTIPLICATION_PRIORITY = 2

    def __init__(self):
        super().__init__(priority=MultiplicationOperation.MULTIPLICATION_PRIORITY)

    def execute(self, operand1: float, operand2: float) -> float:
        """
        Determines the multiplication of two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        return: The multiplication value of operand1 and operand2.
        """
        return operand1 * operand2
