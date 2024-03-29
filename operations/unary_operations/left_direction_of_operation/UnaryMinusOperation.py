from operations.unary_operations.UnaryOperation import UnaryOperation


class UnaryMinusOperation(UnaryOperation):
    """
    Represents the unary minus operation in a calculator.

    extends LeftUnaryOperation. This is similar to NegativeOperation but his priority is not as high.
    """

    UNARY_MINUS_PRIORITY = 2.5
    UNARY_MINUS_PLACEMENT = "Left"

    def __init__(self):
        super().__init__(priority=UnaryMinusOperation.UNARY_MINUS_PRIORITY,
                         placement=UnaryMinusOperation.UNARY_MINUS_PLACEMENT)

    def execute(self, operand: float) -> float:
        """
        Multiplies the provided operand by -1.
        :param operand: The operand as a float.
        :return: the multiplication of the operand by -1.
        """
        return -operand

