class QuizBrain:
    def __init__(self, question_list=None):
        if question_list is None:
            question_list = []
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")
        if answer.lower() == current_question.answer.lower():
            self.score += 1
            print(f"Yay! Good one!\nYour score is currently {self.score}/{self.question_number}\n")
        else:
            print(f"Nah! Too bad!\nYour score is currently {self.score}/{self.question_number}\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def end_of_game(self):
        print("GAME OVER")
        if self.score <= int(len(self.question_list)/2):
                  print("Well, you'll do better next time!")
        if self.score <= int(0.75*len(self.question_list)):
            print("Not bad!")
        else:
            print("Outstanding!")
        print(f"You finished with a score of {self.score}/{len(self.question_list)}\n")

    def play(self):
        while self.still_has_questions():
            self.next_question()
        self.end_of_game()
