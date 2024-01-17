from operations.binary_operations.BinaryOperation import BinaryOperation


class AdditionOperation(BinaryOperation):
    """
    Represents an addition operation in a calculator.
    extents BinaryOperation
    """

    ADDITION_PRIORITY = 1

    def __init__(self):
        super().__init__(priority=AdditionOperation.ADDITION_PRIORITY)

    def execute(self, operand1: float, operand2: float) -> float:
        """
        Performs addition on two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        :return: The result of the addition of operand1 and operand2.
        """
        return operand1 + operand2
