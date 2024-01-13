from operations.binary_operations.BinaryOperation import BinaryOperation
from operations.unary_operations.UnaryOperation import UnaryOperation
from operations.unary_operations.left_direction_of_operation.LeftUnaryOperations import LeftUnaryOperation
from operations.unary_operations.right_direction_of_operation.RightUnaryOperation import RightUnaryOperation
from utills.utills_methods import is_float


class Validator:
    def __init__(self, operations: dict):
        self.operations = operations  # A dictionary of operator and their symbols

    def _is_valid_character(self, ch: str) -> bool:
        return is_float(ch) or self._is_operator(ch) or self._is_parentheses(ch) or ch == "."

    @staticmethod
    def _validate_parentheses(expression: str) -> bool:
        stack = []
        for ch in expression:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if not stack or stack[-1] != '(':
                    raise SyntaxError("Mismatched parentheses )")
                stack.pop()
        if stack:
            raise SyntaxError("Mismatched parentheses (")
        return True

    def _is_operator(self, item):
        return item in self.operations

    @staticmethod
    def _is_open_parentheses(item: str) -> bool:
        return item == "("

    @staticmethod
    def _is_close_parentheses(item: str) -> bool:
        return item == ")"

    def _is_parentheses(self, item: str) -> bool:
        return self._is_open_parentheses(item) or self._is_close_parentheses(item)

    def _extract_numbers(self, input_str: str) -> list[str]:
        extracted_input: list[str] = []
        temp_num: str = ""
        index = 0
        while index < len(input_str):
            if input_str[index] in " \t":
                index += 1
                continue

            if not self._is_valid_character(input_str[index]):
                raise SyntaxError(f"Invalid Character {input_str[index]}")

            if self._is_operator(input_str[index]) or self._is_parentheses(input_str[index]):

                if self._is_open_parentheses(input_str[index]) and temp_num != "":
                    raise SyntaxError(f"Invalid Expression {temp_num}(,\n"
                                      f"operation is needed between the {temp_num} and ( ")

                if (self._is_close_parentheses(input_str[index]) and temp_num == "" and
                        (not self._is_close_parentheses(input_str[index - 1])) and
                        (not self._is_right_unary_operator(input_str[index - 1]))):
                    raise SyntaxError(f"Invalid Position of ) at index {index}")

                if temp_num != "":
                    if is_float(temp_num):
                        extracted_input.append(temp_num)
                    else:
                        raise SyntaxError(f"Invalid Expression {temp_num}")
                temp_num = ""
                extracted_input.append(input_str[index])
            else:  # number
                temp_num += input_str[index]

            index += 1

        if is_float(temp_num):
            extracted_input.append(temp_num)

        return extracted_input

    def _minus_streak(self, input_list: list[str], position: int) -> int:
        counter: int = 0
        while self._is_minus_operation(input_list[position]) and self._is_legal_unary_minus(position, input_list):
            counter += 1
            position += 1
        return counter

    @staticmethod
    def _get_correct_operation(count: int) -> str:
        return "-" if count % 2 == 1 else "+"

    def _is_binary_minus(self, index: int, input_list: list[str]) -> bool:
        if (index > 0 and (is_float(input_list[index - 1])
                           or self._is_right_unary_operator(input_list[index - 1])
                           or self._is_close_parentheses(input_list[index - 1]))):
            return True
        return False

    def _is_legal_unary_minus(self, index: int, input_list: list[str]):
        if index == len(input_list) - 1:
            raise SyntaxError(f"Invalid Position of {input_list[index]} in index {index}")

        if (not self._is_open_parentheses(input_list[index + 1]) and
                not is_float(input_list[index + 1]) and
                not self._is_minus_operation(input_list[index + 1])):
            raise SyntaxError(f"Invalid position of {input_list[index + 1]} after the minus in index {index}")

        return True

    def _handle_minuses(self, input_list: list[str]) -> list[str]:
        minus_handled: list[str] = []
        i = 0
        while i < len(input_list):
            if not self._is_minus_operation(input_list[i]):
                minus_handled += [input_list[i]]
                i += 1
                continue

            # binary minus
            if self._is_binary_minus(i, input_list):
                minus_handled += input_list[i]
                i += 1
                continue

            minus_streak: int = self._minus_streak(input_list, i)
            correct_operation: str = self._get_correct_operation(minus_streak)

            # add the unary operation
            if i == 0:
                if self._is_minus_operation(correct_operation):
                    minus_handled += "_"
                i += minus_streak
                continue

            # add the minus to the number -> unary minus
            if (self._is_binary_operator(input_list[i - 1]) or
                    self._is_left_unary_operator(input_list[i - 1]) or
                    self._is_open_parentheses(input_list[i - 1])):

                if not is_float(input_list[i + minus_streak]) and (not input_list[i + minus_streak] == "("):
                    raise SyntaxError(
                        f"Invalid Position of {input_list[i + minus_streak]} after the -\nin index {i + minus_streak}")

                if input_list[i + minus_streak] == "(":
                    if correct_operation == "-":
                        minus_handled += "~"

                else:
                    if correct_operation == "-":
                        minus_handled += [-float(input_list[i + minus_streak])]
                    else:
                        minus_handled += input_list[i + minus_streak]
                    i += 1

                i += minus_streak

        return minus_handled

    def _is_binary_operator(self, op: str) -> bool:
        return isinstance(self.operations.get(op, None), BinaryOperation)

    def _is_unary_operator(self, op: str) -> bool:
        return isinstance(self.operations.get(op, None), UnaryOperation)

    def _is_right_unary_operator(self, op: str) -> bool:
        return isinstance(self.operations.get(op, None), RightUnaryOperation)

    def _is_left_unary_operator(self, op: str) -> bool:
        return isinstance(self.operations.get(op, None), LeftUnaryOperation)

    @staticmethod
    def _is_minus_operation(op: str) -> bool:
        return op == "-"

    def _validate_operators(self, input_list: list[str]) -> bool:
        num_count: int = 0
        binary_operators_count: int = 0
        for item in input_list:
            if is_float(item):
                num_count += 1
            elif self._is_binary_operator(item):
                binary_operators_count += 1

        return num_count == binary_operators_count + 1

    def _validate_binary_operators(self, input_list: list[str]) -> (bool, str, int):
        index: int = 0
        while index < len(input_list):
            if not self._is_minus_operation(input_list[index]) and not self._is_binary_operator(input_list[index]):
                index += 1
                continue
            elif self._is_binary_operator(input_list[index]) and not self._is_minus_operation(input_list[index]):
                if index == 0 or index == len(input_list) - 1:
                    return False, input_list[index], index

                if (not is_float(input_list[index - 1])) and (not self._is_close_parentheses(input_list[index - 1]) and
                                                              not self._is_right_unary_operator(input_list[index - 1])):
                    return False, input_list[index - 1], index - 1

                if (not is_float(input_list[index + 1])) and (not self._is_open_parentheses(input_list[index + 1]) and
                                                              not self._is_left_unary_operator(
                                                                  input_list[index + 1]) and
                                                              not self._is_minus_operation(input_list[index + 1])):
                    return False, input_list[index + 1], index + 1

            elif self._is_minus_operation(input_list[index]):
                if index == len(input_list) - 1:
                    return False, input_list[index], index

                if (not is_float(input_list[index + 1] and (not self._is_minus_operation(input_list[index + 1]) and
                                                            not self._is_open_parentheses(input_list[index + 1]) and
                                                            not self._is_left_unary_operator(input_list[index + 1])))):
                    return False, input_list[index + 1], index + 1
            index += 1
        return True, None, None

    def _validate_unary_operators(self, input_list: list[str]) -> (bool, str, int):
        index: int = 0
        while index < len(input_list):
            if not self._is_unary_operator(input_list[index]):
                index += 1
                continue

            elif self._is_left_unary_operator(input_list[index]):
                if index == 0:
                    index += 1
                    continue

                if index == len(input_list) - 1:
                    return False, input_list[index], index

                if not self._is_binary_operator(input_list[index - 1]):
                    return False, input_list[index], index

                if (not is_float(input_list[index + 1]) and (not self._is_open_parentheses(input_list[index + 1]) and
                                                             not self._is_minus_operation(input_list[index + 1]))):
                    return False, input_list[index + 1], index + 1

            elif self._is_right_unary_operator(input_list[index]):
                if index == len(input_list) - 1:
                    index += 1
                    continue

                if index == 0:
                    return False, input_list[index], index

                if not is_float(input_list[index - 1]) and not (self._is_close_parentheses(input_list[index - 1])):
                    return False, input_list[index - 1], index - 1

                if (not self._is_right_unary_operator(input_list[index + 1]) and
                        (not self._is_binary_operator(input_list[index + 1])) and
                        (not self._is_close_parentheses(input_list[index + 1]))):
                    return False, input_list[index + 1], index + 1

            index += 1

        return True, None, None

    def validate(self, input_str: str) -> list[str]:
        if not self._validate_parentheses(input_str):
            return []

        extracted_input: list[str] = self._extract_numbers(input_str)

        if not extracted_input:
            raise SyntaxError("Empty Expression")

        valid, item, index = self._validate_unary_operators(extracted_input)
        if not valid:
            raise SyntaxError(f"Invalid Position of {item} in index {index}")

        valid, item, index = self._validate_binary_operators(extracted_input)
        if not valid:
            raise SyntaxError(f"Invalid Position of {item} in index {index}")

        after_minus = self._handle_minuses(extracted_input)
        if self._validate_operators(after_minus):
            return after_minus
        else:
            raise SyntaxError(f"Operators does not match the operands amount")
