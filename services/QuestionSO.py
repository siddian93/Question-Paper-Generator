import random


difficultyLevels = ['easy', 'medium', 'hard']
question = []


def generate_question():
    i = random.randint(0, 2)
    level = difficultyLevels[i]
    if i == 0:
        marks = random.randint(1, 4)
    elif i == 1:
        marks = random.randint(3, 8)
    else:
        marks = random.randint(7, 10)
    return [level, marks]


def get_question(data):
    question.append(data[0])
    question.append(data[1])
    question.append(data[2])
    return question
