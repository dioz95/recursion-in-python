## How Recursion works?
"""
1. A method calls it self
2. Exit from infinite loop
3. Methods stored in stack memmory (last in first out)
def recursionMethod(parameters):
    if exit from condition satisfied:
        return some value
    else:
        recursionMethod(modified params)
"""
print('='*50)
print('How Recursion Works?')
print('='*50)

def firstMethod():
    secondMethod()
    print('I am the first Method')

def secondMethod():
    thirdMethod()
    print('I am the second Method')

def thirdMethod():
    fourthMethod()
    print('I am the third Method')

def fourthMethod():
    print('I am the fourth Method')

firstMethod()

print('='*50)

def recursiveMethod(n):
    if n < 1:
        print('n is less than 1')
    else:
        recursiveMethod(n-1)
        print(n)

recursiveMethod(4)

## Recursion vs Iteration
"""
When to use recursion?
    - Whe can easily breakdown a problem into a similar subproblem
    - When we are fine with extra overhead (both time and space) that comes with it
    - When we need a quick working solution instead of efficient one
    - When traverse a tree 
    - When we use memoization in recursion

When avoid recursion?
    - If time and space complexity
    - Recursion uses more memory. If we use embedded memmory.
    For example and application that takes more memory in the phone is not eficient
    - Recursion can be slow
"""
print('='*50)
print('Recursion vs Iteration')
print('='*50)

def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

print(f'recursive : {powerOfTwo(9)}')

def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power

print(f'iterative : {powerOfTwoIt(9)}')

## How to write recursion in 3 steps?
"""
Case study : Factorial
1. Identify the recursive case (flow)
    n! = n * (n-1) * (n-2) * (n-3) * ... * 1
    n! = n * (n-1)! # recursive case
2. Identify base case (stopiing criterion)
    0! = 1
    1! = 0
3. Identify unintentional case (the constraint)
    - Negative input
    - Float input
"""
print('='*50)
print('How to write recursion in 3 steps?')
print('='*50)

def factorial(n):
    assert n>=0 and int(n) == n, 'The number must be positive or integer only!' # 3. Constraint
    if n in [0,1]: # 2. Base case
        return 1
    else:
        return n * factorial(n-1) # 1. recursive case

print(factorial(4)) 

## How to find Fibonacci numbers using recursion?
"""
1. Recursive Case
    f(n) = f(n-1) + f(n-2)
2. Base condition
    n = 0 & n = 1
3. Unintentional case
    n is float or n is negative

"""
def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be negative or non integer'
    if n == 1 :
        return 1
    elif n == 0 :
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = 10


print('='*50)
print('Print Fibonacci sequence')
print('='*50)

# Print sequence
for i in range(n_terms):
    print(fibonacci(i))

print('='*50)
print('Print Fibonacci list')
print('='*50)

# Display sequence in a list
list_fib = []

for i in range(n_terms):
    list_fib.append(fibonacci(i))
print(list_fib)