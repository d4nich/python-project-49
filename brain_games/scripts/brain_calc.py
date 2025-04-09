#!/usr/bin/env python3
import prompt
import random
def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    n = 0
    while n < 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operation = random.choice(['+', '-', '*'])
        expression = f'{num1} {operation} {num2}'
        result = eval(expression)
        print(f'Question: {expression}')
        answer = int(prompt.string('Your answer: '))
        if result == answer:
            n += 1
            if n<3:
                print('Correct!')
            else:
                print(f'Congratulations, {name}!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}.\nLet's try again, {name}")
            break

if __name__ == '__main__':
    main()