Here is a Python code for calculating the factorial of a given number:
```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")
```
This code defines a recursive function `factorial` that takes an integer `n` as input. If `n` is 0, the function returns 1 (since the factorial of 0 is defined to be 1). Otherwise, the function calls itself with `n-1` as input, and multiplies the result by `n`.

The code then prompts the user to enter a number, calculates the factorial of that number using the `factorial` function, and prints the result.

Alternatively, you can also write an iterative version of the factorial function using a loop:
```
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")
```
This code uses a loop to calculate the factorial, starting from 1 and multiplying the result by each integer up to `n`.