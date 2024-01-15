from operations.binary_operations.AdditionOperation import AdditionOperation
from operations.binary_operations.AverageOperator import AverageOperation
from operations.binary_operations.DivisionOperation import DivisionOperation
from operations.binary_operations.MaximumOperation import MaximumOperation
from operations.binary_operations.MinimumOperation import MinimumOperation
from operations.binary_operations.ModuloOperation import ModuloOperation
from operations.binary_operations.MultiplicationOperation import MultiplicationOperation
from operations.binary_operations.PowerOperation import PowerOperation
from operations.binary_operations.SubtractionOperation import SubOperation
from operations.unary_operations.left_direction_of_operation.UnaryMinusOperation import UnaryMinusOperation
from operations.unary_operations.right_direction_of_operation.FactorialOperation import FactorialOperation
from operations.unary_operations.left_direction_of_operation.NegativeOperation import NegativeOperation
from operations.unary_operations.right_direction_of_operation.SumDigitsOperation import SumDigitsOperation


class OperationsFactory:
    """
    This class represents the operations factory.
    the class has a dictionary of the operation class, and their symbol
    """
    operations = {
        '+': AdditionOperation(),
        '-': SubOperation(),
        '*': MultiplicationOperation(),
        '/': DivisionOperation(),
        '^': PowerOperation(),
        '_': UnaryMinusOperation(),
        '%': ModuloOperation(),
        '@': AverageOperation(),
        '$': MaximumOperation(),
        '&': MinimumOperation(),
        '~': NegativeOperation(),
        '!': FactorialOperation(),
        '#': SumDigitsOperation(),
    }

    def get_operation(self, operator: str):
        """
        Returns the operation class associated with a given operator symbol.

        :param operator: A string representing the operator symbol.
        :return: An instance of the operation class associated with the given operator.
        :raises ValueError: If the operator is not in the operations' dictionary.
        """

        if operator in self.operations.keys():
            return self.operations.get(operator)
        else:
            raise ValueError(f"Unknown operator: {operator}")
