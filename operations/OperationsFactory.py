from operations.binary_operations.AddOperation import AddOperation
from operations.binary_operations.AvgOperator import AvgOperation
from operations.binary_operations.DivOperation import DivOperation
from operations.binary_operations.MaxOperation import MaxOperation
from operations.binary_operations.MinOperation import MinOperation
from operations.binary_operations.ModOperation import ModOperation
from operations.binary_operations.MultOperation import MultOperation
from operations.binary_operations.PowOperation import PowOperation
from operations.binary_operations.SubOperation import SubOperation
from operations.unary_operations.left_direction_of_operation.UnaryMinusOperation import UnaryMinusOperation
from operations.unary_operations.right_direction_of_operation.FactorialOperation import FactorialOperation
from operations.unary_operations.left_direction_of_operation.NegOperation import NegOperation


class OperationsFactory:
    operations = {
        '+': AddOperation(),
        '-': SubOperation(),
        '*': MultOperation(),
        '/': DivOperation(),
        '^': PowOperation(),
        '_': UnaryMinusOperation(),
        '%': ModOperation(),
        '@': AvgOperation(),
        '$': MaxOperation(),
        '&': MinOperation(),
        '~': NegOperation(),
        '!': FactorialOperation(),
    }

    def get_operation(self, operator: str):
        if operator in self.operations.keys():
            return self.operations.get(operator)
        else:
            raise ValueError(f"Unknown operator: {operator}")
