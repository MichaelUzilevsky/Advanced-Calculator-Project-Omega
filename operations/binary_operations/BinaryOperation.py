from operations.IOperation import IOperation


class BinaryOperation(IOperation):
    def priority(self) -> int:
        pass

    def perform(self, operand1: float, operand2: float) -> float:
        pass