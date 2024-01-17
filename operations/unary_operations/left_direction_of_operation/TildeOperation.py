from operations.unary_operations.UnaryOperation import UnaryOperation


class TildeOperation(UnaryOperation):
    """
    Represents the tilde operation in a calculator, changes the sign of the operand.
    Extends LeftUnaryOperation.
    """

    TILDE_PRIORITY = 6
    TILDE_PLACEMENT = "Left"

    def __init__(self):
        super().__init__(priority=TildeOperation.TILDE_PRIORITY,
                         placement=TildeOperation.TILDE_PLACEMENT)

    def execute(self, operand: float) -> float:
        """
        Multiplies the provided operand by -1.
        :param operand: The operand as a float.
        :return: The multiplication value of the operand by -1.
        """
        return -operand
