import random
rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
def get_round():
    num = random.randint(1, 50)
    question = f'Question: {num}'
    for i in range(1, num):
        if num % i == 0 and i != num and i != 1:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return question, correct_answer