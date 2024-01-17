class Operation:
    """
    Base class for mathematical operations in a calculator.
    This class serves as a template for various types of operations, both unary and binary.
    It requires subclasses to implement the priority and perform methods.
    """

    def __init__(self, priority: float):
        self._priority = priority

    def priority(self) -> float:
        """
        returns the priority level of the operation.
        """
        return self._priority

    def execute(self, *operands: float) -> float:
        """
        Performs the mathematical operation on the given operands.
        :param operands: Not fixed number of operands on which the operation will be performed.
        :return: The result of the operation as a float.
        """
        pass
