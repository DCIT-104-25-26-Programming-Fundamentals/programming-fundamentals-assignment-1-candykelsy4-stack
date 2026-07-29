def get_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def get_average(numbers):
    return get_sum(numbers) / len(numbers)

def get_maximum(numbers):
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum

def get_minimum(numbers):
    minimum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n
    return minimum

def main():
    count = int(input("How many numbers? "))
    if count <= 0:
        print("Error: Please enter a positive integer.")
        return

    numbers = []
    for i in range(1, count + 1):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)

    print("\nResults:")
    print(f"Sum:     {get_sum(numbers)}")
    print(f"Average: {get_average(numbers)}")
    print(f"Maximum: {get_maximum(numbers)}")
    print(f"Minimum: {get_minimum(numbers)}")

main()