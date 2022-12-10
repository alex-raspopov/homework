print('\n--- Task 1 ---\n')  # A Person class
# Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old.')


person1 = Person('Carl', 'Johnson', 26)
person1.talk()


print('\n--- Task 2 ---\n')  # Doggy age
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.


class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor


dog1 = Dog(10)
print(f'Dog is {dog1.age} years old that is {dog1.human_age()} in human equivalent')

print('\n--- Task 3 ---\n')  # TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
#
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
#
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.



class TVController:
    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.channel_index = 0

    def first_channel(self):  # turns on the first channel from the list.
        self.channel_index = 0
        return TVController.current_channel(self)

    def last_channel(self):  # turns on the last channel from the list.
        self.channel_index = len(self.channel_list) - 1
        return TVController.current_channel(self)

    def turn_channel(self, num):  # turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
        self.channel_index = num-1
        return TVController.current_channel(self)

    def next_channel(self):  # turns on the next channel. If the current channel is the last one, turns on the first channel.
        if self.channel_index + 1 == len(self.channel_list):
            return TVController.first_channel(self)
        self.channel_index = self.channel_index + 1
        return TVController.current_channel(self)

    def previous_channel(self):  # turns on the previous channel. If the current channel is the first one, turns on the last channel.
        if self.channel_index - 1 < 0:
            return TVController.last_channel(self)
        self.channel_index = self.channel_index - 1
        return TVController.current_channel(self)

    def current_channel(self):  # returns the name of the current channel.
        return self.channel_list[self.channel_index]

    def is_exist(self, find):  # gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
        if find in range(1, len(self.channel_list)+1) or str(find) in self.channel_list:
            return 'Yes'
        return 'No'

# TEST #


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)


def test(func):

    def decor_non_arg(func):
        func()
        print(f"{func.__name__.split('.')[0]}: {controller.channel_list[controller.channel_index]} | index: {controller.channel_index} \t {controller.channel_list}")

    def decor_arg(func):
        def decor(x):
            func(x)
            print(f"{func.__name__.split('.')[0]}({x}): {controller.channel_list[controller.channel_index]} | index: {controller.channel_index} \t {controller.channel_list}")
        return decor
    try:
        return decor_non_arg(func)
    except TypeError:
        return decor_arg(func)


test(controller.first_channel)
test(controller.last_channel)
test(controller.turn_channel)(1)
test(controller.next_channel)
test(controller.next_channel)
test(controller.next_channel)
test(controller.previous_channel)
test(controller.previous_channel)
test(controller.previous_channel)
test(controller.next_channel)
test(controller.current_channel)
print(controller.is_exist('TV1000'))
print(controller.is_exist(3))
print(controller.is_exist('3'))
print(controller.is_exist(0))
