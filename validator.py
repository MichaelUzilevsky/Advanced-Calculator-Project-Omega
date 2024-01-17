from operations.binary_operations.BinaryOperation import BinaryOperation
from operations.unary_operations.UnaryOperation import UnaryOperation
from utills.utills_methods import is_float, is_open_parentheses, is_close_parentheses, is_parentheses, is_operator


class Validator:
    def __init__(self, operations: dict):
        """
        initialize the validator class, with all the possible operations
        :param operations: a dictionary of operations and their symbol
        """
        self.operations = operations  # A dictionary of operator and their symbols

    @staticmethod
    def _is_valid_character(ch: str) -> bool:
        """
        validates if a given char is legal.
        :param ch: string representing operand, operator, parentheses, and .
        :return: true if the char is legal false otherwise
        """
        return is_float(ch) or is_operator(ch) or is_parentheses(ch) or ch in " \t."

    @staticmethod
    def _validate_parentheses(expression: str) -> bool:
        """
        validates the parentheses are ordered correctly in the expression, its using stack to
        match each opening ( to his closed one
        :param expression:
        :return: true if the order of the parentheses is legal, false otherwise
        :raise SyntaxError is the position of the parentheses is not valid
        """
        stack = []
        for ch in expression:
            if is_open_parentheses(ch):
                stack.append(ch)
            elif is_close_parentheses(ch):
                if not stack or not is_open_parentheses(stack[-1]):
                    raise SyntaxError("Mismatched closing parentheses")
                stack.pop()
        if stack:
            raise SyntaxError("Mismatched opening parentheses")
        return True

    def _extract_numbers(self, input_str: str) -> list[str]:
        """
        Extracts numbers and operators from a string input and returns them as a list.
        :param input_str: representing the mathematical expression
        :return: the extracted list where each operand or operator is an item in the list.;
        :raise SyntaxError if character is not valid, if parentheses position is not valid,
                        or if the string representation of numbers is not valid.

        """
        extracted_input: list[str] = []
        temp_num: str = ""
        index = 0
        while index < len(input_str):
            # skip white space characters if not in number
            if input_str[index] in " \t" and not temp_num:
                index += 1
                continue

            # if is not valid, stop
            if not self._is_valid_character(input_str[index]):
                raise SyntaxError(f"Invalid Character {input_str[index]}")

            if is_operator(input_str[index]) or is_parentheses(input_str[index]):
                # open parentheses after a number
                if is_open_parentheses(input_str[index]) and temp_num != "":
                    raise SyntaxError(f"Invalid Expression {temp_num}(,\n"
                                      f"operation is needed between the {temp_num} and ( ")
                # close parentheses after not after number or right unary or close parentheses
                if (is_close_parentheses(input_str[index]) and temp_num == "" and
                        (not is_close_parentheses(input_str[index - 1])) and
                        (not self._is_right_unary_operator(input_str[index - 1]))):
                    raise SyntaxError(f"Invalid Position of ) at index {index}")

                if temp_num:
                    # check if the str can be represented as float
                    if is_float(temp_num):
                        extracted_input.append(temp_num)
                    else:
                        raise SyntaxError(f"Invalid Expression {temp_num}")
                temp_num = ""
                # add the number
                extracted_input.append(input_str[index])
            else:  # generate number
                temp_num += input_str[index]

            index += 1

        # at the end, add to the list if legal, if not raise an error
        if temp_num and not is_float(temp_num):
            raise SyntaxError(f"Invalid Expression {temp_num}")
        if is_float(temp_num):
            extracted_input.append(temp_num)

        return extracted_input

    def _minus_streak(self, input_list: list[str], position: int) -> int:
        """
        counts the minus streak from a given position.
        :param input_list: the given expression
        :param position: the index to start counting from
        :return: the nuber of the minuses in the streak
        """
        counter: int = 0
        while self._is_minus_operation(input_list[position]) and self._is_legal_unary_minus(position, input_list):
            counter += 1
            position += 1
        return counter

    @staticmethod
    def _get_correct_operation(count: int) -> str:
        """
        return + is the count is even, or - otherwise.
        :param count: int
        :return: + is the count is even, or - otherwise
        """
        return "-" if count % 2 == 1 else "+"

    def _is_binary_minus(self, index: int, input_list: list[str]) -> bool:
        """
        returns if the current minus position is a binary minus
        :param index: in the expression where it's going to check.
        :param input_list: the mathematical expression

        :return: true if the current position in the expression is represented as a binary minus, false otherwise
        """
        if (index > 0 and (is_float(input_list[index - 1])
                           or self._is_right_unary_operator(input_list[index - 1])
                           or is_close_parentheses(input_list[index - 1]))):
            return True
        return False

    def _is_legal_unary_minus(self, index: int, input_list: list[str]):
        """
        returns if the current minus position is a unary minus
       :param index: in the expression where it's going to check.
        :param input_list: the mathematical expression
        :return: true if the current position in the expression is represented as a unary minus, false otherwise
        """
        if index == len(input_list) - 1:
            raise SyntaxError(f"Invalid Position of {input_list[index]} in index {index}")

        if (not is_open_parentheses(input_list[index + 1]) and
                not is_float(input_list[index + 1]) and
                not self._is_minus_operation(input_list[index + 1])):
            raise SyntaxError(f"Invalid position of {input_list[index + 1]} after the minus in index {index}")

        return True

    def _handle_minuses(self, input_list: list[str]) -> list[str]:
        """
        Validates the input expression, its differentiate between unary and binary minus operations, remove duplicates
        and more.
        :param input_list: the given expression
        :return: a list where all the minuses are handled
        :raise SyntaxError if the minus is not in a legal position
        """
        minus_handled: list[str] = []
        i = 0
        while i < len(input_list):

            # if not a minus, add it and move to the next item
            if not self._is_minus_operation(input_list[i]):
                minus_handled += [input_list[i]]
                i += 1
                continue

            # binary minus
            if self._is_binary_minus(i, input_list):
                minus_handled += input_list[i]
                i += 1
                continue

            # calculate the minus streak
            minus_streak: int = self._minus_streak(input_list, i)
            correct_operation: str = self._get_correct_operation(minus_streak)

            # add the unary operation
            if i == 0 or is_open_parentheses(input_list[i - 1]):
                if self._is_minus_operation(correct_operation):
                    minus_handled += "_"
                i += minus_streak
                continue

            # add the minus to the number -> unary minus
            if (self._is_binary_operator(input_list[i - 1]) or
                    self._is_left_unary_operator(input_list[i - 1]) or
                    is_open_parentheses(input_list[i - 1])):

                if (not is_float(input_list[i + minus_streak]) and
                        (not is_open_parentheses(input_list[i + minus_streak]))):
                    raise SyntaxError(
                        f"Invalid Position of {input_list[i + minus_streak]} after the -\nin index {i + minus_streak}")

                # only if correct operation is minus, it is added
                if correct_operation == "-":
                    minus_handled += ["--"]

                i += minus_streak

        return minus_handled

    def _is_binary_operator(self, op: str) -> bool:
        """
        return true if the given char is represented by a binary operation
        :param op: char
        :return: true if op is instance of binary operation
        """
        return isinstance(self.operations.get(op, None), BinaryOperation)

    def _is_unary_operator(self, op: str) -> bool:
        """
        return true if the given char is represented by a unary operation
        :param op: char
        :return: true if op is instance of unary operation
        """
        return isinstance(self.operations.get(op, None), UnaryOperation)

    def _is_right_unary_operator(self, op: str) -> bool:
        """
        return true if the given char is represented by a right unary operation
        :param op: char
        :return: true if op is instance of right unary operation
        """
        return (isinstance(self.operations.get(op, None), UnaryOperation) and
                self.operations.get(op).placement() == UnaryOperation.RIGHT)

    def _is_left_unary_operator(self, op: str) -> bool:
        """
        return true if the given char is represented by a left unary operation
        :param op: char
        :return: true if op is instance of left unary operation
        """
        return (isinstance(self.operations.get(op, None), UnaryOperation) and
                self.operations.get(op).placement() == UnaryOperation.LEFT)

    @staticmethod
    def _is_minus_operation(op: str) -> bool:
        return op == "-"

    def _validate_operators(self, input_list: list[str]) -> bool:
        """
        validates the amount of the operators related to the operands, if operator + 1 != operands,
        false is returned
        :param input_list: the expression as a list
        :return: true if the ratio between operators to operands is legal
        """
        num_count: int = 0
        binary_operators_count: int = 0
        for item in input_list:
            if is_float(item):
                num_count += 1
            elif self._is_binary_operator(item):
                binary_operators_count += 1

        return num_count == binary_operators_count + 1

    def _validate_binary_operators(self, input_list: list[str]) -> (bool, str, int):
        """
        Validates all the binary operation in the extracted list.
        Its checks if the position of each char is legal based on what is before and after him.
        :param input_list: the extracted list
        :return: true, null, null  if the position of all the binary operation is legal,
         otherwise false, incorrect char, index of the char that not in his legal position.
        """
        index: int = 0
        while index < len(input_list):
            # not binary operator
            if not self._is_minus_operation(input_list[index]) and not self._is_binary_operator(input_list[index]):
                index += 1
                continue

            # binary but not minus
            elif self._is_binary_operator(input_list[index]) and not self._is_minus_operation(input_list[index]):
                if index == 0 or index == len(input_list) - 1:
                    return False, input_list[index], index
                # before not a number or ) or right unary, raise error
                if (not is_float(input_list[index - 1])) and (not is_close_parentheses(input_list[index - 1]) and
                                                              not self._is_right_unary_operator(input_list[index - 1])):
                    return False, input_list[index - 1], index - 1
                # after not a number or ( or left unary, or minus raise error
                if (not is_float(input_list[index + 1])) and (not is_open_parentheses(input_list[index + 1]) and
                                                              not self._is_left_unary_operator(
                                                                  input_list[index + 1]) and
                                                              not self._is_minus_operation(input_list[index + 1])):
                    return False, input_list[index + 1], index + 1

            # minus
            else:
                if index == len(input_list) - 1:
                    return False, input_list[index], index
                # after not a number or ( or left unary or minus raise error
                if (not is_float(input_list[index + 1] and (not self._is_minus_operation(input_list[index + 1]) and
                                                            not is_open_parentheses(input_list[index + 1]) and
                                                            not self._is_left_unary_operator(input_list[index + 1])))):
                    return False, input_list[index + 1], index + 1
            index += 1
        return True, None, None

    def _validate_unary_operators(self, input_list: list[str]) -> (bool, str, int):
        """
        Validates all the unary operation in the extracted list.
        Its checks if the position of each char is legal based on what is before and after him.
        :param input_list: the extracted list
        :return: true, null, null  if the position of all the unary operation is legal,
         otherwise false, incorrect char, index of the char that not in his legal position.
        """
        index: int = 0
        while index < len(input_list):
            if not self._is_unary_operator(input_list[index]):
                index += 1
                continue

            # left unary
            elif self._is_left_unary_operator(input_list[index]):
                if index == 0:
                    index += 1
                    continue

                if index == len(input_list) - 1:
                    return False, input_list[index], index

                # if before there isn't a binary operation
                if not self._is_binary_operator(input_list[index - 1]):
                    return False, input_list[index], index

                # if after there isn't a number, (, or minus operation
                if (not is_float(input_list[index + 1]) and (not is_open_parentheses(input_list[index + 1]) and
                                                             not self._is_minus_operation(input_list[index + 1]))):
                    return False, input_list[index + 1], index + 1

            else:
                if index == len(input_list) - 1:
                    index += 1
                    continue

                if index == 0:
                    return False, input_list[index], index
                # if before there isn't a number, ) or right unary operation
                if (not is_float(input_list[index - 1]) and
                        not (is_close_parentheses(input_list[index - 1])) and
                        not (self._is_right_unary_operator(input_list[index - 1]))):
                    return False, input_list[index - 1], index - 1

                # if after there isn't a right unary operation, binary operation, or )
                if (not self._is_right_unary_operator(input_list[index + 1]) and
                        (not self._is_binary_operator(input_list[index + 1])) and
                        (not is_close_parentheses(input_list[index + 1]))):
                    return False, input_list[index + 1], index + 1

            index += 1

        return True, None, None

    def validate(self, input_str: str) -> list[str]:
        """
        combines all the validation function above, if error occurs it is raised to the caller,
         if there are no errors the exacted list is returned
        :param input_str: the string expression
        :return: a valid list expression
        """
        # check the parentheses
        if not self._validate_parentheses(input_str):
            return []

        # extracts the str to list
        extracted_input: list[str] = self._extract_numbers(input_str)

        # if not empty list
        if not extracted_input:
            raise SyntaxError("Empty Expression")

        # checks unary operations raises errors if needed
        valid, item, index = self._validate_unary_operators(extracted_input)
        if not valid:
            raise SyntaxError(f"Invalid Position of {item} in index {index}")

        # checks binary operations raises errors if needed
        valid, item, index = self._validate_binary_operators(extracted_input)
        if not valid:
            raise SyntaxError(f"Invalid Position of {item} in index {index}")

        # handles the minuses
        after_minus = self._handle_minuses(extracted_input)

        # checks the ratio between unary and binary operations
        if self._validate_operators(after_minus):
            return after_minus
        else:
            raise SyntaxError(f"Operators does not match the operands amount")
