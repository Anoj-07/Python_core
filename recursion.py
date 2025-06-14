def add_one(num):

#base case
    if num >= 9:
        return num + 1
    # main logic
    total = num + 1
    print(total)

    return add_one(total)

# total = add_one(0)
# print(total)


#Example 1: Factorial 
def factorial(n):
    if n == 0:
        return 1
    
    else:
        return n * factorial(n - 1)

print(factorial(5))

#Example 2: Fibonacci Sequence 
def fib(n):
    if n <= 1:
        return n 
    
    else: 
        return fib(n - 1) + fib(n - 2)

print(fib(8))