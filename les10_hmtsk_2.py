# Task 2
# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

def calc():
    a = input('Enter number (a): ')
    b = input('Enter number (b): ')
    try:
        a = int(a)
        b = int(b)
        c = a ** 2 / b
        return str(f'({a} ^2) / {b} = {c}')
    except ValueError:
        return str('Not a number was entered')
    except ZeroDivisionError:
        return str('Cannot divide by zero')


print(calc())
