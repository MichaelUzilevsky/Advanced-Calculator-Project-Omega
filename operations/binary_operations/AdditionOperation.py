from operations.binary_operations.BinaryOperation import BinaryOperation


class AdditionOperation(BinaryOperation):
    """
    Represents an addition operation in a calculator.
    extents BinaryOperation
    """
    def priority(self) -> int:
        """
        Returns the priority of the addition operation.
        """
        return 1

    def perform(self, operand1: float, operand2: float) -> float:
        """
        Performs addition on two operands.
        :param operand1: The first operand as a float.
        :param operand2: The second operand as a float.
        :return: The result of the addition of operand1 and operand2.
        """
        return operand1 + operand2
