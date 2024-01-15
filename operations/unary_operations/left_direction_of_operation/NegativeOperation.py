from operations.unary_operations.left_direction_of_operation.LeftUnaryOperations import LeftUnaryOperation


class NegativeOperation(LeftUnaryOperation):
    """
    Represents the tilde operation in a calculator, changes the sign of the operand.
    Extends LeftUnaryOperation.
    """

    def priority(self) -> int:
        """
        Returns the priority level of the negation operation.
        """
        return 6

    def perform(self, operand: float) -> float:
        """
        Multiplies the provided operand by -1.
        :param operand: The operand as a float.
        :return: The multiplication value of the operand by -1.
        """
        return -operand

