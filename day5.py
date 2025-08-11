def calculator():
    print("Simple Python Calculator")
    print("Available operations: +, -, *, /")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ").strip()
            num2 = float(input("Enter second number: "))
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation.")
                continue
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

calculator()
