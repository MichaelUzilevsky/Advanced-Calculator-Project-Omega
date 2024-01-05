from evaluator import Evaluator
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
from parser import Parser
from validator import Validator


def main():
    pass


operations = {
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

if __name__ == '__main__':
    validator = Validator(operations)
    parser = Parser(operations)
    evaluator = Evaluator()
    input_str = "3 @ 4 @ 5"
    input_lst = validator.validate(input_str)
    postfix_lst = parser.to_postfix(input_lst)
    result = evaluator.evaluate(postfix_lst)
    print(result)



