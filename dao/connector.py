import csv


class Connector:

    def write_header(self):
        with open('../data/questionsDB.csv', mode='a+') as f:
            fieldnames = ['Question Number', 'level', 'marks']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

    def last_question_number(self):
        count = 1
        reader = csv.DictReader(open("../data/questionsDB.csv"))
        for raw in reader:
            print raw
            count = count+1
        return count

    def write_question(self, question):
        questionDetails = {
            'Question Number':  self.last_question_number(),
            'level': question[0],
            'marks': question[1]
        }
        with open('../data/questionsDB.csv', mode='a+') as f:
            fieldnames = ['Question Number', 'level', 'marks']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(questionDetails)
            f.close()

    def read_last_question(self):
        pass

    def read_all_question(self):
        f = open("../data/questionsDB.csv")
        reader = csv.DictReader(f)
        count = 0
        questions = []
        for raw in reader:
            if count == 0:
                count += 1
                pass
            questions.append(raw)
        f.close()
        return questions

    def read_first_question(self):
        pass

    def read_question(self, ques_no):
        pass

    def write_questions(n):
        pass

    def __init__(self):
        pass
        #self.write_header()