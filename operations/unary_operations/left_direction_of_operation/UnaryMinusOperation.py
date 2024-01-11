from operations.unary_operations.left_direction_of_operation.LeftUnaryOperations import LeftUnaryOperation


class UnaryMinusOperation(LeftUnaryOperation):

    def priority(self) -> float:
        return 2.5

    def perform(self, operand: float) -> float:
        return -operand

