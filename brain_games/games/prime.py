import random
rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_round():
    num = random.randint(1, 50)
    question = f'Question: {num}'
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer