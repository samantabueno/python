#Program to show Fibonacci sequence

number = int(input('Type a number limit to Fibonacci Sequence: '))
c = 1
fibonacci_number = 1
before_number = 0
before_before_number = 0
while c <= number + 1:
    if c == 1:
        print(before_number, '->', fibonacci_number, end = ' ')
    else:
        print('->', fibonacci_number, end = ' ')
    c = c + 1
    before_before_number = before_number
    before_number = fibonacci_number
    fibonacci_number = before_number + before_before_number
