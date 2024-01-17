from operations.OperationsFactory import OperationsFactory
from operations.binary_operations.BinaryOperation import BinaryOperation
from operations.unary_operations.UnaryOperation import UnaryOperation
from utills.utills_methods import is_float


class Evaluator:
    """
    this class's purpose is to evaluate a postfix expression
    """
    def evaluate(self, postfix: list[str]) -> float:
        """
        this function receives a postfix expression and returns its solution
        :param postfix: list[str] that represent valid postfix expression
        :return: the solution of this expression
        :raise ZeroDivisionError if there is a division by 0
        :raise ValueError if there is an attempt to factorial negative or float number
        """
        solution_stack = []
        factory = OperationsFactory()
        result: float = 0

        for item in postfix:
            if is_float(item):
                solution_stack.append(float(item))
            else:
                operation = factory.get_operation(item)
                if isinstance(operation, UnaryOperation):
                    operand = solution_stack.pop()
                    result = operation.execute(operand)
                elif isinstance(operation, BinaryOperation):
                    operand2 = solution_stack.pop()
                    operand1 = solution_stack.pop()
                    result = operation.execute(operand1, operand2)

                solution_stack.append(result)

        return solution_stack.pop()


