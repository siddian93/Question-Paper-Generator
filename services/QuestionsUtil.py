import random as rand


def remove_questions(easy_marks, med_marks, hard_mark,  cur_mark, max_mark, selected, all):
    res = False
    while cur_mark != max_mark  and res != False:
        res = False
        if hard_mark > 30 and ((hard_mark-30) >=7):
            diff = hard_mark-30
            for question in selected[2]:
                if int(question['marks']) == diff:
                    res = True
                    question['isUsed'] = 0
                    selected[2].remove(question)
                    cur_mark = cur_mark - diff
                    hard_mark = easy_marks-diff
                    break

        if med_marks > 50 and ((med_marks-50) >= 3):
            diff = med_marks - 50
            for question in selected[1]:
                if int(question['marks']) == diff:
                    res = True
                    question['isUsed'] = 0
                    selected[1].remove(question)
                    cur_mark = cur_mark - diff
                    med_marks = med_marks-diff
                    break

        if (easy_marks > 20) and ((easy_marks - 20) >= 1):
            diff = easy_marks - 20
            for question in selected[0]:
                if int(question['marks']) >= diff:
                    res = True
                    question['isUsed'] = 0
                    selected[0].remove(question)
                    cur_mark = cur_mark - diff
                    easy_marks = easy_marks-diff
                    break
    #print cur_mark, easy_marks, med_marks, hard_mark
    return selected, easy_marks, med_marks, hard_mark, cur_mark


    """
    net_remove = cur_mark - 100
    res = False
    if hard_mark > 30:
        diff = hard_mark-30
        if ( diff >= 7):
            for question in selected[2]:
                if int(question['marks']) == diff:
                    res = True
                    question['isUsed'] = 0
                    selected[2].remove(question)
                    cur_mark = cur_mark - diff
                    break
    if med_marks > 50:
        diff = med_marks-50
        if (diff >= 3):
            for question in selected[1]:
                if int(question['marks']) == diff:
                    res = True
                    question['isUsed'] = 0
                    selected[1].remove(question)
                    cur_mark = cur_mark-diff
                    break
    if easy_marks > 20:
        diff = easy_marks-20
        if diff >= 1:
            for question in selected[0]:
                if int(question['marks']) == diff:
                    res = True
                    question['isUsed'] = 0
                    selected[0].remove(question)
                    cur_mark = cur_mark - diff
                    break
                elif int(question['marks']) > diff:
                    res = True
                    question['isUsed'] = 0
                    selected[0].remove(question)
                    cur_mark = cur_mark - diff
                    break
    #print diff, res, cur_mark
    return selected
    """

def add_questions(easy_marks, med_marks, hard_mark, cur_mark, selected, all):

    pass


def segrgateQuestions(questions):
    easy = []
    hard = []
    medium = []
    marks_based = {}
    for data in questions:
        data['isUsed'] = 0
        if data['level'] == 'easy':
            easy.append(data)
        elif data['level'] == 'medium':
            medium.append(data)
        else:
            hard.append(data)

        mark_index = int(data['marks'])
        if mark_index in marks_based.keys():
            marks_based[mark_index].append(data)
        else:
            marks_based[mark_index] = []
            marks_based[mark_index].append(data)
    return [easy, medium, hard, marks_based]


def createQuestionPaper(data,  max_marks):
    questions = []
    easy_ques = []
    med_ques = []
    hard_ques = []
    question = {}
    curr_marks = 0
    easy_marks = 0
    med_marks = 0
    hard_mark = 0
    while curr_marks < 20:
        selector = rand.randint(0, len(data[0])-1)
        #print selector, len(data[0])
        if data[0][selector]['isUsed'] == 0:
            curr_marks = curr_marks+int(data[0][selector]['marks'])
            question = data[0][selector]
            easy_ques.append(question)
            data[0][selector]['isUsed'] = 1
    easy_marks = curr_marks
    #print easy_ques, '\n',curr_marks

    while curr_marks < 70:
        selector = rand.randint(0, len(data[1]) - 1)
        #print selector, len(data[1])
        if data[1][selector]['isUsed'] == 0:
            curr_marks = curr_marks + int(data[1][selector]['marks'])
            question = data[1][selector]
            med_ques.append(question)
            data[1][selector]['isUsed'] = 1
    med_marks = curr_marks-easy_marks
    #print med_ques, '\n', curr_marks

    while curr_marks < 100:
        selector = rand.randint(0, len(data[2]) - 1)
        #print selector, len(data[1])
        if data[2][selector]['isUsed'] == 0:
            curr_marks = curr_marks + int(data[2][selector]['marks'])
            question = data[2][selector]
            hard_ques.append(question)
            data[2][selector]['isUsed'] = 1
    hard_mark = curr_marks - easy_marks - med_marks
    #print hard_ques, '\n', curr_marks
    questions.append(easy_ques)
    questions.append(med_ques)
    questions.append(hard_ques)
    if curr_marks > 100:
        questions = remove_questions(easy_marks, med_marks, hard_mark, curr_marks, max_marks, questions, data)
    elif curr_marks < 100:
        questions = add_questions(easy_marks, med_marks, hard_mark, curr_marks, max_marks, questions, data)
    else:
        pass

    #print easy_marks, med_marks, hard_mark, curr_marks
    return questions