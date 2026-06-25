# recursion is the process which a funtion calls itself directly or indirectly. The corresponding function is called as recursive function. Recursion is used to solve problems which can be broken down into smaller sub-problems of the same type. It is a common programming technique that allows a function to call itself in order to solve a problem.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

def print_numbers(n):

    if n == 0:
        return

    print(n)

    print_numbers(n-1)

print_numbers(5)
# Dry Run of print_numbers(5):
# print_numbers(5)

# Print 5
# Call print_numbers(4)

# Print 4
# Call print_numbers(3)

# Print 3
# Call print_numbers(2)

# Print 2
# Call print_numbers(1)

# Print 1
# Call print_numbers(0)

# Stop

# Factorial of 5 is 120
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print("Factorial of 5 is", factorial(5))
# factorial(5)

# = 5 × factorial(4)

# = 5 × 4 × factorial(3)

# = 5 × 4 × 3 × factorial(2)

# = 5 × 4 × 3 × 2 × factorial(1)

# = 5 × 4 × 3 × 2 × 1

# = 120


# sum of two numbers using recursion
def sum_of_two_numbers(a, b):
    if b == 0:
        return a
    else:
        return sum_of_two_numbers(a + 1, b - 1)

print("Sum of 5 and 3 is", sum_of_two_numbers(5, 3))