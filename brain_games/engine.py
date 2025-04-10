import prompt
def run_game(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_module.rules)
    n = 0
    while n < 3:
        question, correct_answer = game_module.get_round()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            n += 1
            if n<3:
                print('Correct!')
            else:
                print(f'Congratulations, {name}!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\nLet's try again, {name}")
            break