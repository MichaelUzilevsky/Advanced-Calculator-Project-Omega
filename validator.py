from operations.binary_operations.BinaryOperation import BinaryOperation
from operations.unary_operations.UnaryOperation import UnaryOperation
from utills.utills_methods import is_float


class Validator:
    def __init__(self, operations: dict):
        self.operations = operations  # A dictionary of operator and their symbols

    def _is_valid_character(self, ch: str) -> bool:
        return is_float(ch) or ch in self.operations or ch in ".()"

    def _validate_parentheses(self, expression: str) -> bool:
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

    def _extract_numbers(self, input_str: str) -> list[str]:
        extracted_input: list[str] = []
        temp_num: str = ""
        for ch in input_str:
            if ch in " ":
                continue
            if not self._is_valid_character(ch):
                raise SyntaxError(f"Invalid Character {ch}")
            if self._is_operator(ch) or ch in "()":

                if ch == "(" and temp_num != "":
                    raise SyntaxError(f"Invalid Expression {temp_num} ( ... ,"
                                      f"operation is needed between the {temp_num} and ( ")

                if (ch == ")" and temp_num == "" and
                        ((input_str.index(ch) - 1) > 0 and input_str[input_str.index(ch)] != ")")):
                    raise SyntaxError(f"Invalid Position of )")

                if temp_num != "":
                    if is_float(temp_num):
                        extracted_input.append(temp_num)
                    else:
                        raise SyntaxError(f"Invalid Expression {temp_num}")
                temp_num = ""
                extracted_input.append(ch)
            else:  # number
                temp_num += ch

        if is_float(temp_num):
            extracted_input.append(temp_num)

        return extracted_input

    def _minus_streak(self, input_list: list[str], position: int) -> int:
        counter: int = 0
        while input_list[position] == "-":
            counter += 1
            position += 1
        return counter

    def _get_correct_operation(self, count: int) -> str:
        return "-" if count % 2 == 1 else "+"

    def _handle_minuses(self, input_list: list[str]) -> list[str]:
        minus_handled: list[str] = []
        i = 0
        while i < len(input_list):
            if input_list[i] != "-":
                minus_handled += [input_list[i]]
                i += 1
                continue
            # keep the operator, not adding the operator to the number
            m_streak: int = self._minus_streak(input_list, i)
            correct_operation: str = self._get_correct_operation(m_streak)
            # add the minus to the number
            if i == 0 or self._is_binary_operator(input_list[i - 1]) or input_list[i - 1] in "~(":

                if not is_float(input_list[i + m_streak]) and (not input_list[i + m_streak] == "("):
                    raise SyntaxError(
                        f"Invalid Position of {input_list[i + m_streak]} after the -\nin index {i + m_streak}")

                if input_list[i + m_streak] == "(":
                    if correct_operation == "-":
                        minus_handled += "~"

                else:
                    if correct_operation == "-":
                        minus_handled += [-float(input_list[i + m_streak])]
                    else:
                        minus_handled += input_list[i + m_streak]
                    i += 1

                i += m_streak

            # minus is not part of the number
            elif i > 0 and is_float(input_list[i - 1]) or input_list[i - 1] in ")!":
                minus_handled += correct_operation
                i += m_streak

        return minus_handled

    def _is_binary_operator(self, op: str) -> bool:
        return isinstance(self.operations.get(op, None), BinaryOperation)

    def _is_unary_operator(self, op: str) -> bool:
        return isinstance(self.operations.get(op, None), UnaryOperation)

    def _is_minus_operation(self, op: str) -> bool:
        return op == "-"

    # after minus handle
    def _validate_operators(self, input_list: list[str]) -> bool:
        num_count: int = 0
        binary_operators_count: int = 0
        for item in input_list:
            if is_float(item):
                num_count += 1
            elif self._is_binary_operator(item):
                binary_operators_count += 1

        return num_count == binary_operators_count + 1

    # before minus handle
    def _validate_binary_operators(self, input_list: list[str]) -> (bool, str, int):
        index: int = 0
        while index < len(input_list):
            if not self._is_minus_operation(input_list[index]) and not self._is_binary_operator(input_list[index]):
                index += 1
                continue
            elif self._is_binary_operator(input_list[index]) and not self._is_minus_operation(input_list[index]):
                if index == 0 or index == len(input_list) - 1:
                    return False, input_list[index], index

                if (not is_float(input_list[index - 1])) and (not input_list[index - 1] in ")!"):
                    return False, input_list[index], index

                if (not is_float(input_list[index + 1])) and (not input_list[index + 1] in "(~-"):
                    return False, input_list[index], index

            elif self._is_minus_operation(input_list[index]):
                if index == len(input_list) - 1:
                    return False, input_list[index], index

                if (input_list[index + 1] not in "-(~") and (not is_float(input_list[index + 1])):
                    return False, input_list[index], index
            index += 1
        return True, None, None

    def _validate_unary_operators(self, input_list: list[str]) -> (bool, str, int):
        index: int = 0
        while index < len(input_list):
            if not self._is_unary_operator(input_list[index]):
                index += 1
                continue

            elif input_list[index] == "~":
                if index == 0:
                    index += 1
                    continue

                if index == len(input_list) - 1:
                    return False, input_list[index], index

                if not self._is_binary_operator(input_list[index - 1]):
                    return False, input_list[index], index

                if (not input_list[index + 1] in "(-") and (not is_float(input_list[index + 1])):
                    return False, input_list[index], index

            elif input_list[index] == "!":
                if index == len(input_list) - 1:
                    index += 1
                    continue

                if index == 0:
                    return False

                if (input_list[index - 1] not in ")") and (not is_float(input_list[index - 1])):
                    return False, input_list[index], index

                if (input_list[index + 1] not in "!") and (not self._is_binary_operator(input_list[index + 1])):
                    return False, input_list[index], index

            index += 1

        return True, None, None

    def validate(self, input_str: str) -> list[str]:
        if not self._validate_parentheses(input_str):
            return []

        extracted_input: list[str] = self._extract_numbers(input_str)

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
