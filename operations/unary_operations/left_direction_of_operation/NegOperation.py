from operations.unary_operations.left_direction_of_operation.LeftUnaryOperations import LeftUnaryOperation


class NegOperation(LeftUnaryOperation):

    def priority(self) -> int:
        return 6

    def perform(self, operand: float) -> float:
        return -operand

