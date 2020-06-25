# Exercise for training functions
# Program that sort numbers, save in a list
# and then returns the sum of even numbers


from time import sleep
import random


def sort(sorted_numbers):
    print('Sorting ...')
    sleep(1)
    for c in range(1, 5):
        sorted_numbers.append(random.randint(1, 10))
    print(f'Numbers sorted are: {sorted_numbers}.')
    sleep(1)


def sum_even_num(sorted_numbers):
    sum = 0
    for v in sorted_numbers:
        if v % 2 == 0:
            sum += v
    print(f'The sum of even numbers is {sum}.')


numbers = list()
sort(numbers)
sum_even_num(numbers)

