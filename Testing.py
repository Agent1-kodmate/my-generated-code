Here is the final updated code:
```python
def FACTORIAL(m):
    if m == 0 or m == 1:
        return 1
    else:
        return m * FACTORIAL(m-1)

print("The factorial of 5 is", FACTORIAL(5))
```