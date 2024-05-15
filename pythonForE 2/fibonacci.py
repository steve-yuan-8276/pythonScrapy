# write Fibonacci series up to n
def fib(n):    
    """Print a Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # see below
        a, b = b, a + b
    return result

n = int(input('enter a integer greater then 2:'))
print(fib(n))
