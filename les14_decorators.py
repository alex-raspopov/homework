print('---- Task 1 ----\n')
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#  "add called with 4, 5"
# ```
# def logger(func):
#     pass
# @logger
# def add(x, y):
#     return x + y
# @logger
# def square_all(*args):
#     return [arg ** 2 for arg in args]
# ```

from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args):
        return print(f'{func.__name__}{args}')
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(1, 2, 3, 4, 5)


print('\n---- Task 2 ----\n')
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
# ```
# def stop_words(words: list):
#     pass
# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
# ```


def stop_words(words: list):
    def decor_pass_func(func):
        @wraps(func)
        def decor_pass_arg(args):
            to_do = func(args)
            for search in words:
                to_do = to_do.replace(search, '*')
            return to_do
        return decor_pass_arg
    return decor_pass_func


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Steve"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"



print('\n---- Task 3 ----\n')
# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
# ```
# def arg_rules(type_: type, max_length: int, contains: list):
#     pass
# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:
#     return f"{name} drinks pepsi in his brand new BMW!"
# assert create_slogan('johndoe05@gmail.com') is False
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
# ```


# def arg_rules(type_: type, max_length: int, contains: list):  # v1 (basic)
#     def decor_pass_func(func):
#         @wraps(func)
#         def decor_pass_arg(args):
#             if len(args) > max_length:
#                 return 'max_length'
#             if type(args) != type_:
#                 return 'type_'
#             for words in contains:
#                 if words not in args:
#                     return 'contains'
#             return func(args)
#         return decor_pass_arg
#     return decor_pass_func

def arg_rules(type_: type, max_length: int, contains: list):  # v2 (error list)
    def decor_pass_func(func):
        @wraps(func)
        def decor_pass_arg(args):
            errors = []
            if len(str(args)) > max_length:
                errors.append(f'Max length: {max_length}')
            if type(args) != type_:
                errors.append(f'Type must be: {type_.__name__}')
            for words in contains:
                if words not in str(args):
                    errors.append(f'Must contain: {contains}')
                    break
            if errors:
                return f'Error: {errors}'
            del errors
            return func(args)
        return decor_pass_arg
    return decor_pass_func


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('S@SH05'))
print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('johndoe@gmail.com'))
print(create_slogan('S@SH0'))
print(create_slogan(12313132))

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'