from calculator import Calculator


def main():
    calculator = Calculator()

    while True:
        user_input = input("Enter expression (or type 'exit' to quit):\n")

        if user_input.lower() == 'exit':
            break

        try:
            result = calculator.calculate(user_input)
            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
