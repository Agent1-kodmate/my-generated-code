Here is a simple Python code to calculate the factorial of a given number:
```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)
```
This code defines a recursive function `factorial` that takes an integer `n` as input. If `n` is 0, the function returns 1 (since the factorial of 0 is defined to be 1). Otherwise, the function calls itself with `n-1` as input, and multiplies the result by `n`.

The code then prompts the user to enter a number, calculates the factorial of that number using the `factorial` function, and prints the result.

Alternatively, you can use a loop to calculate the factorial, like this:
```
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)
```
This code uses a loop to iterate from 1 to `n`, multiplying the result by each integer in the range. The final result is returned by the function.

Both of these codes will work correctly for positive integers. Let me know if you have any questions or need further modifications!