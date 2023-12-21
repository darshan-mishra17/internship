def fibonacciSeries(n):
    fib_series = [0, 1] 

    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series

n = int(input("Enter the value of n: "))


fibonacciTerms = fibonacciSeries(n)
print("Fibonacci Series:")
for term in fibonacciTerms:
    print(term, end=" ")
