import random
import math
rules = 'Find the greatest common divisor of given numbers.'
def get_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    expression = math.gcd(num1, num2)
    correct_answer = str(expression)
    question = f'Question: {num1} {num2}'
    return question, correct_answer