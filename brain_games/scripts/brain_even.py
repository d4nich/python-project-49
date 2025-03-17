#!/usr/bin/env python3
import prompt
import random
def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    while n < 3:
        iseven = ''
        num = random.randint(1, 100)
        print(num)
        if num % 2 == 0:
            iseven = 'yes'
        else:
            iseven = 'no'
        answer = prompt.string('Your answer: ')
        if iseven == answer:
            n += 1
            if n<3:
                print('Correct!')
            else:
                print(f'Congratulations, {name}!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {iseven}.\nLet's try again, {name}")
            break

if __name__ == '__main__':
    main()