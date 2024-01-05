from evaluator import Evaluator
from parser import Parser
from validator import Validator
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


class Calculator:
    def __init__(self):
        self._operations = {
            '+': AddOperation(),
            '-': SubOperation(),
            '*': MultOperation(),
            '/': DivOperation(),
            '^': PowOperation(),
            '%': ModOperation(),
            '@': AvgOperation(),
            '$': MaxOperation(),
            '&': MinOperation(),
            '~': NegOperation(),
            '!': FactorialOperation(),
        }

        self._validator = Validator(self._operations)
        self._parser = Parser(self._operations)
        self._evaluator = Evaluator()

    def calculate(self, input_str: str) -> float:
        input_lst = self._validator.validate(input_str)
        postfix_lst = self._parser.to_postfix(input_lst)
        result = self._evaluator.evaluate(postfix_lst)
        return result
