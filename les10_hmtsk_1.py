# Task 1
# (1) Write a function called oops that explicitly raises an IndexError exception when called.
# (2) Then write another function that calls oops inside a try/except statement to catch the error.
# (3) What happens if you change oops to raise KeyError instead of IndexError?

def oops(a):  # (1) Write a function called oops that explicitly raises an IndexError exception when called.
    return a[len(a)+1]


def oops2(a):  # (2) Then write another function that calls oops inside a try/except statement to catch the error.
    try:
        return oops(a)
    except IndexError:
        return ('Ooops. IndexError')
    except KeyError:  # (3) What happens if you change oops to raise KeyError instead of IndexError?
        return ('Ooops. KeyError')


# oops(input('Enter smths: '))  # (1) function raises an IndexError exception when called.
# print(oops2(input('Enter smths: ')))  # (2) function that calls oops inside a try/except statement to catch the error.

ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
print(oops2(ages))  # (3) What happens if you change oops to raise KeyError instead of IndexError?

