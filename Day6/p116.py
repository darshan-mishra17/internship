def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

n = int(input("Enter the value of n: "))

fibonacciTerms = fibonacci(n)

print("Fibonacci Series:")
for term in fibonacciTerms:
    print(term, end=" ")
