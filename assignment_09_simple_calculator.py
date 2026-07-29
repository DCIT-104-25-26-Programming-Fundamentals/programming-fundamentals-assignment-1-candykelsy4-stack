def print_menu():
    print("\n============================")
    print("       SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def exponentiate(a, b):
    return a ** b

def get_inputs():
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    return a, b

def main():
    operations = {
        "1": (add,          "+"),
        "2": (subtract,     "-"),
        "3": (multiply,     "*"),
        "4": (divide,       "/"),
        "5": (modulus,      "%"),
        "6": (exponentiate, "**"),
    }

    while True:
        print_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in operations:
            func, symbol = operations[choice]
            a, b = get_inputs()
            if symbol in ("/", "%") and b == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = func(a, b)
                a_display = int(a) if a == int(a) else a
                b_display = int(b) if b == int(b) else b
                print(f"Result: {a_display} {symbol} {b_display} = {result}")
        else:
            print("Error: Invalid choice. Please select a number between 1 and 7.")

main()