from calculator import Calculator
from operations.Operation import Operation
from operations.unary_operations.UnaryOperation import UnaryOperation
from operations.unary_operations.left_direction_of_operation.UnaryMinusOperation import UnaryMinusOperation


def main():
    calculator = Calculator()
    try:
        while True:
            user_input = input("Enter expression (or type 'exit' to quit):\n")

            if user_input.lower() == 'exit':
                break

            try:
                result = calculator.calculate(user_input)
                print(f"Result: {result}\n")

            except Exception as e:
                print(f"Error: {e}")

    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")


if __name__ == '__main__':
    main()
