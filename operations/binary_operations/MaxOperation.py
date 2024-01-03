from operations.binary_operations.BinaryOperation import BinaryOperation


class MaxOperation(BinaryOperation):
    def priority(self) -> int:
        return 5

    def perform(self, operand1: float, operand2: float) -> float:
        return max(operand1, operand2)
