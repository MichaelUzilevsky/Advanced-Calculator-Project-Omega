from operations.Operation import Operation


class UnaryOperation(Operation):
    """
    Base class for unary operations in a calculator.
    extends Operation
    Unary operations operate on a single operand.
    """

    LEFT = "Left"
    RIGHT = "Right"
    VALID_PLACEMENTS = (LEFT, RIGHT)

    def __init__(self, priority: float, placement: str):
        super().__init__(priority)
        if placement not in UnaryOperation.VALID_PLACEMENTS:
            raise ValueError(f"The placement of the unary operation must be in {self.VALID_PLACEMENTS}")
        self._placement = placement

    def placement(self) -> str:
        """
        returns the placement of the operation (LEFT or RIGHT) unary operation.
        """
        return self._placement

    def execute(self, operand: float) -> float:
        """
        Performs the unary operation on the given operand.
        :param operand: The operand as a float on which the operation will be performed.
        :return: The result of the operation as a float.
        """
        pass
