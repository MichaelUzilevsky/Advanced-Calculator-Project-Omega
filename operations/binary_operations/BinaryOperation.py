from operations.Operation import Operation


class BinaryOperation(Operation):
    def priority(self) -> int:
        pass

    def perform(self, operand1: float, operand2: float) -> float:
        pass