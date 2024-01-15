from operations.unary_operations.UnaryOperation import UnaryOperation


class LeftUnaryOperation(UnaryOperation):
    """
    Base class for left unary operations in a calculator.
    extends Operation
    act as a marker class
    """

    def priority(self) -> int:
        """
        returns the priority level of the operation.
        """
        pass

    def perform(self, operand: float) -> float:
        """
        Performs the unary operation on the given operand.
        :param operand: The operand as a float on which the operation will be performed.                :return: The result of the operation as a float.
        """
        pass

