from operations.unary_operations.UnaryOperation import UnaryOperation


class NegOperation(UnaryOperation):

    def priority(self):
        return 6

    def perform(self, operand):
        return -operand
