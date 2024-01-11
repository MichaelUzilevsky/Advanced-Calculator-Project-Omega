from operations.binary_operations.BinaryOperation import BinaryOperation


class PowerOperation(BinaryOperation):
    def priority(self) -> int:
        return 3

    def perform(self, operand1: float, operand2: float) -> float:
        return operand1 ** operand2
