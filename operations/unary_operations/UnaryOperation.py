from operations.Operation import Operation


class UnaryOperation(Operation):
    def priority(self) -> int:
        pass

    def perform(self, operand: float) -> float:
        pass

