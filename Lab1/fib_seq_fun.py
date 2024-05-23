def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

fib_sequence = fibonacci_series(num_terms)
print(f"The first {num_terms} terms of the Fibonacci series are: {fib_sequence}")
