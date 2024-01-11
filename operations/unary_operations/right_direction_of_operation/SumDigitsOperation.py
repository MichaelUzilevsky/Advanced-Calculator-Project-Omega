from operations.unary_operations.right_direction_of_operation.RightUnaryOperation import RightUnaryOperation


class SumDigitsOperation(RightUnaryOperation):
    def priority(self) -> int:
        return 6

    @staticmethod
    def _remove_decimal_point(number: float) -> str:
        # Convert the number to a string
        number_str = str(number)
        # Remove the decimal point
        number_str = number_str.replace('.', '')
        # Convert the string back to an integer
        return number_str

    def perform(self, operand: float) -> int:
        negative = 1
        if operand < 0:
            negative = -1
            operand *= -1

        number_str = self._remove_decimal_point(operand)
        sum_digits = 0
        for digit in number_str:
            sum_digits += int(digit)

        return sum_digits * negative

