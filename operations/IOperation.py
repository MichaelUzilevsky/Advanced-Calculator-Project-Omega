class IOperation:
    def priority(self) -> int:
        pass

    def preform(self, *operands: float) -> float:
        pass
