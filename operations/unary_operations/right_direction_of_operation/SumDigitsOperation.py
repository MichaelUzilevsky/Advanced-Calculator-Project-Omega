from operations.unary_operations.UnaryOperation import UnaryOperation


class SumDigitsOperation(UnaryOperation):
    """
    Represents the operation that sums the digits of a number in a calculator.
    Extends RightUnaryOperation.
    """
    SUM_DIGITS_PRIORITY = 6
    SUM_DIGITS_PLACEMENT = "Right"

    def __init__(self):
        super().__init__(priority=SumDigitsOperation.SUM_DIGITS_PRIORITY,
                         placement=SumDigitsOperation.SUM_DIGITS_PLACEMENT)

    @staticmethod
    def _remove_decimal_point(number: float) -> str:
        """
        Converts a float number to a string and removes the decimal point.
        :param number: The number from which the decimal point is to be removed.
        :return: A string representation of the number without the decimal point.
        """
        number_str = str(number)
        # Remove the decimal point
        number_str = number_str.replace('.', '')
        return number_str

    def execute(self, operand: float) -> float:
        """
        Sums the digits of the given operand.
        :param operand: The operand as a float.
        :return: The sum of the digits of the operand.
        :raise ValueError if operand is negative
        """
        if operand < 0:
            raise ValueError("operand must be non-negative in order to sum its digits")

        number_str = self._remove_decimal_point(operand)

        if "e" in str(operand):
            print(f"\nThe number is represented in a Scientific Notation {operand}."
                  "\nThe Result may not be accurate\n")
            number_str = number_str[0: number_str.index("e")]

        sum_digits = 0
        for digit in number_str:
            if digit.isdigit():
                sum_digits += int(digit)

        return sum_digits
