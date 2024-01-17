from operations.unary_operations.UnaryOperation import UnaryOperation


class SignMinusOperation(UnaryOperation):
    """
    Represents the unary minus operation in a calculator.
    extends LeftUnaryOperation. This is similar to NegativeOperation but his priority is higher.
    """

    SIGN_MINUS_PRIORITY = 8
    SIGN_MINUS_PLACEMENT = "Left"

    def __init__(self):
        super().__init__(priority=SignMinusOperation.SIGN_MINUS_PRIORITY,
                         placement=SignMinusOperation.SIGN_MINUS_PLACEMENT)

    def execute(self, operand: float) -> float:
        """
        Multiplies the provided operand by -1.
        :param operand: The operand as a float.
        :return: the multiplication of the operand by -1.
        """
        return -operand
