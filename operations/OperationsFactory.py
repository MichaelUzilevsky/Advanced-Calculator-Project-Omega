from operations.binary_operations.AddOperation import AddOperation
from operations.binary_operations.AvgOperator import AvgOperation
from operations.binary_operations.DivOperation import DivOperation
from operations.binary_operations.MaxOperation import MaxOperation
from operations.binary_operations.MinOperation import MinOperation
from operations.binary_operations.ModOperation import ModOperation
from operations.binary_operations.MultOperation import MultOperation
from operations.binary_operations.PowOperation import PowOperation
from operations.binary_operations.SubOperation import SubOperation
from operations.unary_operations.FactorialOperation import FactorialOperation
from operations.unary_operations.NegOperation import NegOperation


class OperationsFactory:
    def get_operation(self, operator: str):
        if operator in {"+", "-", "*", "/", "^", "%", "@", "$", "&"}:
            return self._create_binary_operation(operator)
        elif operator in {"~", "!"}:
            return self._create_unary_operation(operator)
        else:
            raise ValueError(f"Unknown operator: {operator}")

    def _create_binary_operation(self, operator: str):
        match operator:
            case '+':
                return AddOperation()
            case '-':
                return SubOperation()
            case '*':
                return MultOperation()
            case '/':
                return DivOperation()
            case '^':
                return PowOperation()
            case '%':
                return ModOperation()
            case '@':
                return AvgOperation()
            case '$':
                return MaxOperation()
            case '&':
                return MinOperation()
            case _:
                raise ValueError(f"Unknown binary operator: {operator}")

    def _create_unary_operation(self, operator: str):
        match operator:
            case '~':
                return NegOperation()
            case '!':
                return FactorialOperation()
            case _:
                raise ValueError(f"Unknown unary operator: {operator}")
