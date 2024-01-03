from operations.binary_operations.BinaryOperation import BinaryOperation


class DivOperation(BinaryOperation):
    def priority(self) -> int:
        return 2

    def perform(self, operand1: float, operand2: float) -> float:
        if operand2 != 0:
            return operand1 / operand2
        raise ZeroDivisionError("Can not Divide by 0")
