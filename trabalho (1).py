
import random


class Questions:
    
    def __init__(self, question, answers, correct_answer,question_type=None, number=None):
        self.number = number
        self.question = question
        self.question_type = question_type
        self.answers = answers
        self.correct_answer = correct_answer



class Question:

    def __init__(self, question, question_type, correct_answer):
        self.question = question
        self.question_type = question_type
        self.answers = []
        self.correct_answer = correct_answer



class Normal(Questions):

    def print_question(self, question, answers):
        print(question)
        print(answers)


class VF(Questions):
   
    def print_question(self, question, answers):
        print(question)
        print(answers)



# from enum import Enum
# class QuestionType(Enum):
#     NORMAL = 1
#     VF = 2


class QuestionFactory:

# 1o Padrao de projeto - FACTORY



    @staticmethod
    def create(q) -> Question:
        
        question_type = q['question_type']
                
        if question_type == 'NORMAL':
            return Normal(q['question'], q['answers'], q['correct_answer'])

        if question_type == 'VF':
            return VF(q['question'], q['answers'], q['correct_answer'])
            
        return None


class Strategy:
    # 2o padrao de projeto - STRATEGY
    @staticmethod
    def ordenar(vetor, option):
        
        if option == StrategyEnum.ORDENADO.value:
           vetor
        else:
            random.shuffle(vetor)
            
        
from enum import Enum
class StrategyEnum(Enum):
    ORDENADO = 1
    EMBARALHAR = 2

        
class Quiz:

    # 3o padrao de projeto - SINGLETON
    _instance = None

    def __init__(self):
        self.resultado = 0
        self.questoes = 0
    

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    
    def criaQuiz(self):

        import json
        
        data = json.load(open('gabarito.json'))
        
        questions = data['questions']
        acertos = 0
        vetor = []
        

        for q in questions:

            question_type = q['question_type']


            if question_type == 'NORMAL':
                normal = QuestionFactory.create(q)
                vetor.append(normal)
                # print(normal.question)

            if question_type == 'VF':
                vf = QuestionFactory.create(q)
                vetor.append(vf)

        # print(vetor)
        option = int(input('1 - Questoes ORDENADAS \n2 - Questoes EMBARALHADAS\n '))

        
        Strategy.ordenar(vetor, option)
        print("\n\n*** ATENCAO ***\n\n")
        print("PARA RESPONDER AS QUESTOES: 0 (PRIMEIRA ALTERNATIVA) ATE 3 (ULTIMA ALTERNATIVA)\n\n")
        for v in vetor:

            
            v.print_question(v.question, v.answers)

            self.questoes += 1


            user_ans = input('Resposta: ').upper()

            if user_ans == v.correct_answer:
                acertos += 1
                print('\nresposta CORRETA!!\n :) proxima questao.\n\n')
            else:
                print('\nresposta ERRADA...\n :( proxima questao. \n\n')

            self.resultado = acertos
            resultado = self.resultado

        return resultado
    

    def print_results(self):
        print(f'\n\nO usuario acertou {self.resultado} de {self.questoes} questoes!')



if __name__ == '__main__':

    q1 = Quiz()

    q1.criaQuiz()
    q1.print_results()
