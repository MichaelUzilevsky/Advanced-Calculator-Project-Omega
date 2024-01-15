from operations.unary_operations.left_direction_of_operation.LeftUnaryOperations import LeftUnaryOperation


class UnaryMinusOperation(LeftUnaryOperation):
    """
    Represents the unary minus operation in a calculator.

    extends LeftUnaryOperation. This is similar to NegativeOperation but his priority is not as high.
    """

    def priority(self) -> float:
        """
        Returns the priority level of the unary minus operation.
        """
        return 2.5

    def perform(self, operand: float) -> float:
        """
        Multiplies the provided operand by -1.
        :param operand: The operand as a float.
        :return: the multiplication of the operand by -1.
        """
        return -operand

