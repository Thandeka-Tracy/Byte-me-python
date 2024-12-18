# Placeholder functions for Python basics, to be implemented later
import math

def add_numbers(a, b):
    return a + b

def find_maximum(a, b, c):
    return max(a, b, c)

def is_palindrome(string):
    try:
        return string == string[::-1]
    except:
        raise(TypeError)

def count_word_occurrences(text, word):
    try:
        split_string = text.lower().split()
        return split_string.count(word)
    except:
        raise(TypeError)


def read_file_lines(filepath):
    with open(filepath) as content:
        return content.readlines()

def factorial(n):
    pass

def is_prime(n):
    if n < 0:
        raise(ValueError)
    elif isinstance(n, str):
        raise(TypeError)
    elif n == 0 or n == 1:
        return False
    else:
        for num in range(2, n):
            if n & num == 0:
                return False
        return True

def sort_numbers(numbers):
    if len(numbers) == 0:
        return numbers
    elif isinstance(numbers[0], str):
        raise(TypeError)
    else:
        return sorted(numbers)

def factorial(n):
    if n < 0:
        raise(ValueError)
    elif isinstance(n, str):
        raise(TypeError)
    elif n == 0 or n == 1:
        return 1
    else:
        product = 1
        for num in range(1, n+1):
            product *= num
        return product

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def tower_of_hanoi(n, source, auxiliary, target):
    
    """
    Solve the Tower of Hanoi problem for n disks.

    Args:
        n (int): Number of disks to move.
        source (str): Name of the source peg.
        auxiliary (str): Name of the auxiliary peg.
        target (str): Name of the target peg.

    Returns:
        list: A list of moves to solve the Tower of Hanoi problem.

    Example:
    >>> tower_of_hanoi(3, 'A', 'B', 'C')
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    """
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        if isinstance(self.name, int) or isinstance(self.age, str):
            raise(TypeError)


if __name__ == "__main__":
    # Placeholder functions for Python basics, to be implemented later
    #to test your functions, you can use the following code
    print(add_numbers(3, 5)) #e.g