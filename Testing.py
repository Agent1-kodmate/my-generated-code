Here is a Python code to check if a given string is a palindrome or not:
```
def is_palindrome(s):
    return s == s[::-1]

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```
Here's how the code works:

* The `is_palindrome` function takes a string `s` as input.
* It checks if the string is equal to its reverse (`s[::-1]`). If they are equal, it means the string is a palindrome.
* The `input` function is used to get a string input from the user.
* The `if` statement checks the result of the `is_palindrome` function and prints a message accordingly.

You can also use a more efficient approach using slicing:
```
def is_palindrome(s):
    return s == ''.join(reversed(s))

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```
This code uses the `reversed` function to reverse the string and then joins the characters back together using the `join` method.

You can also ignore case and whitespace by modifying the code as follows:
```
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```
This code converts the input string to lowercase and removes whitespace characters before checking if it's a palindrome.