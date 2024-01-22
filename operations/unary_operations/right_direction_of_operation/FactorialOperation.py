from operations.unary_operations.UnaryOperation import UnaryOperation


class FactorialOperation(UnaryOperation):
    """
    Represents the factorial operation in a calculator.
    extends RightUnaryOperation.
    """
    FACTORIAL_PRIORITY = 6
    FACTORIAL_PLACEMENT = "Right"

    def __init__(self):
        super().__init__(priority=FactorialOperation.FACTORIAL_PRIORITY,
                         placement=FactorialOperation.FACTORIAL_PLACEMENT)

    def execute(self, operand: int) -> int:
        """
        Calculates the factorial of the provided integer operand.
        :param operand: The operand as an integer.
        :return: The factorial of the operand.
        :raises ValueError: If the operand is not an integer or is less than 0.
        """
        if int(operand) != operand or operand < 0:
            raise ValueError(f"{operand} must be an integer and non-negative to calculate factorial.")
        if 'e' in str(operand):
            raise ValueError(f"the number is too large for evaluating its factorial {operand}")
        if operand == 0:
            return 1
        result: int = 1
        for i in range(1, int(operand) + 1):
            result *= i
        return result




