from operations.IOperation import IOperation


class UnaryOperation(IOperation):
    def priority(self) -> int:
        pass

    def perform(self, operand: float) -> float:
        pass
