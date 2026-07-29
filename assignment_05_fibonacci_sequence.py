def print_fibonacci(n):
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    print("Fibonacci sequence:", " ".join(str(x) for x in sequence))

def is_fibonacci(number):
    if number < 0:
        print(f"{number} is NOT a Fibonacci number.")
        return
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    if a == number:
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")

def main():
    print("--- PART A ---")
    n = int(input("How many terms? "))
    print_fibonacci(n)

    print("\n--- PART B ---")
    number = int(input("Enter a number to check: "))
    is_fibonacci(number)

main()