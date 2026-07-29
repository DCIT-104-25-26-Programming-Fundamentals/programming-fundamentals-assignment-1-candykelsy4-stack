def print_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"  {number}  x  {i}  =  {number * i}")

def print_all_tables(n):
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return
    for number in range(1, n + 1):
        print_table(number)
        if number < n:
            print("---------------------------")

def main():
    print("--- PART A ---")
    number = int(input("Enter a number: "))
    print_table(number)

    print("\n--- PART B ---")
    n = int(input("Enter N to print tables from 1 to N: "))
    print()
    print_all_tables(n)

main()