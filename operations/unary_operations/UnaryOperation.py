from operations.Operation import Operation


class UnaryOperation(Operation):
    """
    Base class for unary operations in a calculator.
    extends Operation
    Unary operations operate on a single operand.
    """
    def priority(self) -> int:
        """
        returns the priority level of the operation.
        """
        pass

    def perform(self, operand: float) -> float:
        """
        Performs the unary operation on the given operand.
        :param operand: The operand as a float on which the operation will be performed.
        :return: The result of the operation as a float.
        """
        pass

