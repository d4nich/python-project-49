import random
rules = 'What number is missing in the progression?'


def get_round():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    lenght = random.randint(5, 11)
    progression = []
    progression = list(range(start, start + step * lenght, step))
    hiden_index = random.randint(0, lenght - 1)
    correct_answer = str(progression[hiden_index])
    progression[hiden_index] = '..'
    progression_str = ' '.join(map(str, progression))
    question = f'Question: {progression_str}'
    return question, correct_answer