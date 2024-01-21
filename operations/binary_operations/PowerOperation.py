from operations.binary_operations.BinaryOperation import BinaryOperation


class PowerOperation(BinaryOperation):
    """
    Represents the power operation in a calculator.
    extents BinaryOperation.
    """

    POWER_PRIORITY = 3

    def __init__(self):
        super().__init__(priority=PowerOperation.POWER_PRIORITY)

    def execute(self, operand1: float, operand2: float) -> float:
        """
        Determines the power of two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        :return: The power value of operand1 and operand2.
        :raise value error if imaginary numbers or division by zero may occur
        """
        if operand1 == 0 and operand2 <= 0:
            raise ValueError(f"Illegal expression {operand1} ^ {operand2}")
        if operand1 < 0 and -1 < operand2 < 1:
            raise ValueError(f"Imaginary numbers are not supported {operand1} ^ {operand2}")

        if int(operand1) != operand1 or int(operand2) != operand2:
            return operand1 ** operand2
        operand1 = int(operand1)
        operand2 = int(operand2)
        return operand1 ** operand2
