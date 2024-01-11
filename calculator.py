from evaluator import Evaluator
from parser import Parser
from validator import Validator
from operations.OperationsFactory import OperationsFactory as Operators


class Calculator:
    def __init__(self):
        self._validator = Validator(Operators.operations)
        self._parser = Parser(Operators.operations)
        self._evaluator = Evaluator()

    def calculate(self, input_str: str) -> float:
        input_lst = self._validator.validate(input_str)
        postfix_lst = self._parser.to_postfix(input_lst)
        result = self._evaluator.evaluate(postfix_lst)
        return result
