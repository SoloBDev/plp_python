# Basic Calculator Program
print("Welcome to the Basic Calculator!")
print("=" * 40)

# Get user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ").strip()
    
    # Perform the operation
    result = None
    
    if operation == '+':
        result = num1 + num2
        print(f"\n{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"\n{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"\n{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("\nError: Division by zero is not allowed!")
        else:
            result = num1 / num2
            print(f"\n{num1} / {num2} = {result}")
    else:
        print(f"\nError: '{operation}' is not a valid operation. Please use +, -, *, or /.")
        
except ValueError:
    print("\nError: Please enter valid numbers!")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")

print("\nThank you for using the calculator!")
