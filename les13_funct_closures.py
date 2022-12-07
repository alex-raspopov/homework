print('--- Task 1 ---\n')
# Write a Python program to detect the number of local variables declared in a function.


def task1():
    a, b, c = 1, 2, 3

    def nested(): return a + b + c
    print(f'Function "{task1.__name__}" has {len(dir())} local variables: {dir()}')


task1()

print('\n--- Task 2 ---\n')
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)


def task2(placeholder):
    def nested(*args):
        res = 0
        for i in args:
            res += i**2
        return print(placeholder, res, f'( sum{args}^2 )')
    return nested


a = task2('Result is:')
a(1, 2, 3)

print('\n--- Task 3 ---\n')
# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]

#  My solution:


def choose_func(nums_list, func1, func2):
    for num in nums_list:
        if num < 0:
            return func2(nums_list)
    return func1(nums_list)


#  Check result

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25], 'Task 3 failed'
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5], 'Task 3 failed'