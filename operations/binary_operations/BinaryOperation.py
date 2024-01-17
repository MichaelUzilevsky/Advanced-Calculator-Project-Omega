from operations.Operation import Operation


class BinaryOperation(Operation):
    """
    Base class for binary operations in a calculator.
    extents Operation.
    """

    def execute(self, operand1: float, operand2: float) -> float:
        """
        performs the binary operation on two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        :return: The result of the operation as a float.
        """
        pass
