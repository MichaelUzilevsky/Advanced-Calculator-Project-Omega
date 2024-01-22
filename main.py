from calculator import Calculator


def main():
    # create instance of the Calculator
    calculator = Calculator()
    # this while runs while the input is not exit or keyboard interrupt occurred.
    try:
        while True:
            user_input = input("Enter expression, or type 'exit' to quit:\n")

            if user_input.lower() == 'exit':
                break

            try:
                result = calculator.calculate(user_input)
                print(f"Result: {result}\n")

            except (SyntaxError, ValueError, ZeroDivisionError, OverflowError) as e:
                print(f"Error: {e}\n")

    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
    except EOFError:
        print("\nEOF, exiting.")


if __name__ == '__main__':
    main()
