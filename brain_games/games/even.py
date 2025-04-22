import random
rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round():
    num = random.randint(1, 100)
    question = f'Question: {num}'
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer