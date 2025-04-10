import random
rules = 'What is the result of the expression?'
def get_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    expression = f'{num1} {operation} {num2}'
    correct_answer = str(eval(expression))
    question = f'Question: {expression}'
    return question, correct_answer