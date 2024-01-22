from operations.binary_operations.BinaryOperation import BinaryOperation


class ModuloOperation(BinaryOperation):
    """
    Represents the modulo operation in the calculator.
    extents BinaryOperation.
    """
    MODULO_PRIORITY = 4

    def __init__(self):
        super().__init__(priority=ModuloOperation.MODULO_PRIORITY)

    def execute(self, operand1: float, operand2: float) -> float:
        """
        Determines the reminder of two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        return: The reminder value of operand1 and operand2.
        """
        if operand2 == 0:
            raise ValueError("Unable to Modulo by zero.")
        return operand1 % operand2
