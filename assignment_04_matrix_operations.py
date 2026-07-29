def read_matrix(name, rows, cols):
    matrix = []
    print(f"Enter {name} ({rows}x{cols}):")
    for i in range(rows):
        while True:
            row = list(map(int, input(f"  Enter row {i + 1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            print(f"  Error: expected {cols} values, got {len(row)}. Try again.")
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("  " + "  ".join(f"{val:4}" for val in row))

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result

def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(a[i][j] + b[i][j])
        result.append(new_row)
    return result

def multiply_matrices(a, b):
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    result = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result

def part_a():
    print("\n--- PART A: Transpose ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix("Matrix", rows, cols)
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transpose(matrix))

def part_b():
    print("\n--- PART B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    a = read_matrix("Matrix A", rows, cols)
    b = read_matrix("Matrix B", rows, cols)
    print("\nMatrix A:")
    print_matrix(a)
    print("\nMatrix B:")
    print_matrix(b)
    print("\nResult (A + B):")
    print_matrix(add_matrices(a, b))

def part_c():
    print("\n--- PART C: Multiply Two Matrices ---")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))
    a = read_matrix("Matrix A", m, n)
    b = read_matrix("Matrix B", n, p)
    print("\nMatrix A:")
    print_matrix(a)
    print("\nMatrix B:")
    print_matrix(b)
    print("\nResult (A x B):")
    print_matrix(multiply_matrices(a, b))

def main():
    part_a()
    part_b()
    part_c()

main()