from operations.binary_operations.BinaryOperation import BinaryOperation


class AdditionOperation(BinaryOperation):
    def priority(self) -> int:
        return 1

    def perform(self, operand1: float, operand2: float) -> float:
        return operand1 + operand2
