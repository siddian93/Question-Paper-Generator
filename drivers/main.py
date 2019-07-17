from dao.connector import Connector as Conn
import services.QuestionsUtil as util

if __name__ == '__main__':
    max_marks = 100
    conn = Conn()
    questions = conn.read_all_question()
    segregated = util.segrgateQuestions(questions)
    question_paper, easy_marks, med_marks, hard_marks, total_marks = util.createQuestionPaper(segregated, max_marks)
    print "Ques Marks Level"
    for questions in question_paper:
        for q in questions:
            print "Q", q['Question Number'], " ", q['marks'], " ", q['level']

    print total_marks,  " ", easy_marks, " ", med_marks, " ", hard_marks
    """
    conn.write_header()
    for i in range(1, 100):
        conn.write_question(Q.generate_question())
    print conn.last_question_number()
    """