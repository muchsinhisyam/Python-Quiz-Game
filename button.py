import pygame.font

class Button():
    def __init__(self, screen):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Load the play button image, resize and get its rect.
        self.play_button = pygame.image.load("images/play_button.png")
        self.play_button = pygame.transform.scale(self.play_button, (200, 200))
        self.rect_play = self.play_button.get_rect()
        # Play button location
        self.rect_play.centerx = self.screen_rect.centerx
        self.rect_play.centery = self.screen_rect.centery  - 50

        # Load the retry button image and get its rect.
        self.play_again = pygame.image.load("images/play_again.png")
        self.rect_play_again = self.play_again.get_rect()
        # Play button location
        self.rect_play_again.centerx = self.screen_rect.centerx
        self.rect_play_again.centery = self.screen_rect.centery + 100

        # Load the next button image and get its rect.
        self.next = pygame.image.load("images/next.png")
        self.rect_next = self.next.get_rect()
        # Play button location
        self.rect_next.centerx = self.screen_rect.centerx + 330
        self.rect_next.centery = self.screen_rect.centery + 270

        # Load the tutorial image and get its rect.
        self.tutorial_img = pygame.image.load("images/tutorial.PNG")
        self.rect_tutorial = self.tutorial_img.get_rect()
        # Tutorial image location
        self.rect_tutorial.centerx = self.screen_rect.centerx - 70
        self.rect_tutorial.centery = self.screen_rect.centery - 20

        # Load the topics button image and get its rect.
        self.operators = pygame.image.load("images/operators.png")
        self.rect_operators = self.operators.get_rect()
        self.array = pygame.image.load("images/array.png")
        self.rect_array = self.array.get_rect()
        self.loops = pygame.image.load("images/loops.png")
        self.rect_loops = self.loops.get_rect()
        # Play button location
        self.rect_operators.centerx = self.screen_rect.centerx + 100
        self.rect_operators.centery = self.screen_rect.centery + 100
        self.rect_array.centerx = self.screen_rect.centerx
        self.rect_array.centery = self.screen_rect.centery
        self.rect_loops.centerx = self.screen_rect.centerx - 100
        self.rect_loops.centery = self.screen_rect.centery - 100

        # Load the question no 1 image and answer and get its rect.
        self.question1 = pygame.image.load("images/question1.PNG")
        self.rect_question1 = self.question1.get_rect()
        self.answer1_a = pygame.image.load("images/answer1_a.PNG")
        self.rect_answer1_a = self.answer1_a.get_rect()
        self.answer1_b = pygame.image.load("images/answer1_b.PNG")
        self.rect_answer1_b = self.answer1_b.get_rect()
        self.answer1_c = pygame.image.load("images/answer1_c.PNG")
        self.rect_answer1_c = self.answer1_c.get_rect()
        # Play button location
        self.rect_question1.centerx = self.screen_rect.centerx
        self.rect_question1.centery = self.screen_rect.centery - 100
        self.rect_answer1_a.centerx = self.screen_rect.centerx
        self.rect_answer1_a.centery = self.screen_rect.centery - 10
        self.rect_answer1_b.centerx = self.screen_rect.centerx
        self.rect_answer1_b.centery = self.screen_rect.centery + 40
        self.rect_answer1_c.centerx = self.screen_rect.centerx
        self.rect_answer1_c.centery = self.screen_rect.centery + 90

        # Load the question no 2 image and answer and get its rect.
        self.question2 = pygame.image.load("images/question2.PNG")
        self.rect_question2 = self.question2.get_rect()
        self.answer2_a = pygame.image.load("images/answer2_a.PNG")
        self.rect_answer2_a = self.answer2_a.get_rect()
        self.answer2_b = pygame.image.load("images/answer2_b.PNG")
        self.rect_answer2_b = self.answer2_b.get_rect()
        self.answer2_c = pygame.image.load("images/answer2_c.PNG")
        self.rect_answer2_c = self.answer2_c.get_rect()
        # Play button location
        self.rect_question2.centerx = self.screen_rect.centerx
        self.rect_question2.centery = self.screen_rect.centery - 100
        self.rect_answer2_a.centerx = self.screen_rect.centerx
        self.rect_answer2_a.centery = self.screen_rect.centery - 10
        self.rect_answer2_b.centerx = self.screen_rect.centerx
        self.rect_answer2_b.centery = self.screen_rect.centery + 40
        self.rect_answer2_c.centerx = self.screen_rect.centerx
        self.rect_answer2_c.centery = self.screen_rect.centery + 90

        # Load the question no 3 image and answer and get its rect.
        self.question3 = pygame.image.load("images/question3.PNG")
        self.rect_question3 = self.question3.get_rect()
        self.answer3_a = pygame.image.load("images/answer3_a.PNG")
        self.rect_answer3_a = self.answer3_a.get_rect()
        self.answer3_b = pygame.image.load("images/answer3_b.PNG")
        self.rect_answer3_b = self.answer3_b.get_rect()
        self.answer3_c = pygame.image.load("images/answer3_c.PNG")
        self.rect_answer3_c = self.answer3_c.get_rect()
        # Play button location
        self.rect_question3.centerx = self.screen_rect.centerx
        self.rect_question3.centery = self.screen_rect.centery - 100
        self.rect_answer3_a.centerx = self.screen_rect.centerx
        self.rect_answer3_a.centery = self.screen_rect.centery - 10
        self.rect_answer3_b.centerx = self.screen_rect.centerx
        self.rect_answer3_b.centery = self.screen_rect.centery + 40
        self.rect_answer3_c.centerx = self.screen_rect.centerx
        self.rect_answer3_c.centery = self.screen_rect.centery + 90

        # Load the question no 4 image and answer and get its rect.
        self.question4 = pygame.image.load("images/question4.PNG")
        self.rect_question4 = self.question4.get_rect()
        self.answer4_a = pygame.image.load("images/answer4_a.PNG")
        self.rect_answer4_a = self.answer4_a.get_rect()
        self.answer4_b = pygame.image.load("images/answer4_b.PNG")
        self.rect_answer4_b = self.answer4_b.get_rect()
        self.answer4_c = pygame.image.load("images/answer4_c.PNG")
        self.rect_answer4_c = self.answer4_c.get_rect()
        # Play button location
        self.rect_question4.centerx = self.screen_rect.centerx
        self.rect_question4.centery = self.screen_rect.centery - 100
        self.rect_answer4_a.centerx = self.screen_rect.centerx
        self.rect_answer4_a.centery = self.screen_rect.centery - 10
        self.rect_answer4_b.centerx = self.screen_rect.centerx
        self.rect_answer4_b.centery = self.screen_rect.centery + 40
        self.rect_answer4_c.centerx = self.screen_rect.centerx
        self.rect_answer4_c.centery = self.screen_rect.centery + 90

        # Load the question no 5 image and answer and get its rect.
        self.question5 = pygame.image.load("images/question5.PNG")
        self.rect_question5 = self.question5.get_rect()
        self.answer5_a = pygame.image.load("images/answer5_a.PNG")
        self.rect_answer5_a = self.answer5_a.get_rect()
        self.answer5_b = pygame.image.load("images/answer5_b.PNG")
        self.rect_answer5_b = self.answer5_b.get_rect()
        self.answer5_c = pygame.image.load("images/answer5_c.PNG")
        self.rect_answer5_c = self.answer5_c.get_rect()
        # Play button location
        self.rect_question5.centerx = self.screen_rect.centerx
        self.rect_question5.centery = self.screen_rect.centery - 100
        self.rect_answer5_a.centerx = self.screen_rect.centerx
        self.rect_answer5_a.centery = self.screen_rect.centery - 10
        self.rect_answer5_b.centerx = self.screen_rect.centerx
        self.rect_answer5_b.centery = self.screen_rect.centery + 40
        self.rect_answer5_c.centerx = self.screen_rect.centerx
        self.rect_answer5_c.centery = self.screen_rect.centery + 90

        # Load the question no 6 image and answer and get its rect.
        self.question6 = pygame.image.load("images/question6.PNG")
        self.rect_question6 = self.question6.get_rect()
        self.answer6_a = pygame.image.load("images/answer6_a.PNG")
        self.rect_answer6_a = self.answer6_a.get_rect()
        self.answer6_b = pygame.image.load("images/answer6_b.PNG")
        self.rect_answer6_b = self.answer6_b.get_rect()
        self.answer6_c = pygame.image.load("images/answer6_c.PNG")
        self.rect_answer6_c = self.answer6_c.get_rect()
        # Play button location
        self.rect_question6.centerx = self.screen_rect.centerx
        self.rect_question6.centery = self.screen_rect.centery - 100
        self.rect_answer6_a.centerx = self.screen_rect.centerx
        self.rect_answer6_a.centery = self.screen_rect.centery - 10
        self.rect_answer6_b.centerx = self.screen_rect.centerx
        self.rect_answer6_b.centery = self.screen_rect.centery + 40
        self.rect_answer6_c.centerx = self.screen_rect.centerx
        self.rect_answer6_c.centery = self.screen_rect.centery + 90

        # Load the question no 7 image and answer and get its rect.
        self.question7 = pygame.image.load("images/question7.PNG")
        self.rect_question7 = self.question7.get_rect()
        self.answer7_a = pygame.image.load("images/answer7_a.PNG")
        self.rect_answer7_a = self.answer7_a.get_rect()
        self.answer7_b = pygame.image.load("images/answer7_b.PNG")
        self.rect_answer7_b = self.answer7_b.get_rect()
        self.answer7_c = pygame.image.load("images/answer7_c.PNG")
        self.rect_answer7_c = self.answer7_c.get_rect()
        # Play button location
        self.rect_question7.centerx = self.screen_rect.centerx
        self.rect_question7.centery = self.screen_rect.centery - 100
        self.rect_answer7_a.centerx = self.screen_rect.centerx
        self.rect_answer7_a.centery = self.screen_rect.centery - 10
        self.rect_answer7_b.centerx = self.screen_rect.centerx
        self.rect_answer7_b.centery = self.screen_rect.centery + 40
        self.rect_answer7_c.centerx = self.screen_rect.centerx
        self.rect_answer7_c.centery = self.screen_rect.centery + 90

        # Load the question no 8 image and answer and get its rect.
        self.question8 = pygame.image.load("images/question8.PNG")
        self.rect_question8 = self.question8.get_rect()
        self.answer8_a = pygame.image.load("images/answer8_a.PNG")
        self.rect_answer8_a = self.answer8_a.get_rect()
        self.answer8_b = pygame.image.load("images/answer8_b.PNG")
        self.rect_answer8_b = self.answer8_b.get_rect()
        self.answer8_c = pygame.image.load("images/answer8_c.PNG")
        self.rect_answer8_c = self.answer8_c.get_rect()
        # Play button location
        self.rect_question8.centerx = self.screen_rect.centerx
        self.rect_question8.centery = self.screen_rect.centery - 100
        self.rect_answer8_a.centerx = self.screen_rect.centerx
        self.rect_answer8_a.centery = self.screen_rect.centery - 10
        self.rect_answer8_b.centerx = self.screen_rect.centerx
        self.rect_answer8_b.centery = self.screen_rect.centery + 40
        self.rect_answer8_c.centerx = self.screen_rect.centerx
        self.rect_answer8_c.centery = self.screen_rect.centery + 90

        # Load the question no 9 image and answer and get its rect.
        self.question9 = pygame.image.load("images/question9.PNG")
        self.rect_question9 = self.question9.get_rect()
        self.answer9_a = pygame.image.load("images/answer9_a.PNG")
        self.rect_answer9_a = self.answer9_a.get_rect()
        self.answer9_b = pygame.image.load("images/answer9_b.PNG")
        self.rect_answer9_b = self.answer9_b.get_rect()
        self.answer9_c = pygame.image.load("images/answer9_c.PNG")
        self.rect_answer9_c = self.answer9_c.get_rect()
        # Play button location
        self.rect_question9.centerx = self.screen_rect.centerx
        self.rect_question9.centery = self.screen_rect.centery - 100
        self.rect_answer9_a.centerx = self.screen_rect.centerx
        self.rect_answer9_a.centery = self.screen_rect.centery - 10
        self.rect_answer9_b.centerx = self.screen_rect.centerx
        self.rect_answer9_b.centery = self.screen_rect.centery + 40
        self.rect_answer9_c.centerx = self.screen_rect.centerx
        self.rect_answer9_c.centery = self.screen_rect.centery + 90

        # Load the question no 10 image and answer and get its rect.
        self.question10 = pygame.image.load("images/question10.PNG")
        self.rect_question10 = self.question10.get_rect()
        self.answer10_a = pygame.image.load("images/answer10_a.PNG")
        self.rect_answer10_a = self.answer10_a.get_rect()
        self.answer10_b = pygame.image.load("images/answer10_b.PNG")
        self.rect_answer10_b = self.answer10_b.get_rect()
        # Play button location
        self.rect_question10.centerx = self.screen_rect.centerx
        self.rect_question10.centery = self.screen_rect.centery - 100
        self.rect_answer10_a.centerx = self.screen_rect.centerx
        self.rect_answer10_a.centery = self.screen_rect.centery - 10
        self.rect_answer10_b.centerx = self.screen_rect.centerx
        self.rect_answer10_b.centery = self.screen_rect.centery + 40

        # Load the question no 11 image and answer and get its rect.
        self.question11 = pygame.image.load("images/question11.PNG")
        self.rect_question11 = self.question11.get_rect()
        self.answer11_a = pygame.image.load("images/answer11_a.PNG")
        self.rect_answer11_a = self.answer11_a.get_rect()
        self.answer11_b = pygame.image.load("images/answer11_b.PNG")
        self.rect_answer11_b = self.answer11_b.get_rect()
        self.answer11_c = pygame.image.load("images/answer11_c.PNG")
        self.rect_answer11_c = self.answer11_c.get_rect()
        # Play button location
        self.rect_question11.centerx = self.screen_rect.centerx
        self.rect_question11.centery = self.screen_rect.centery - 100
        self.rect_answer11_a.centerx = self.screen_rect.centerx
        self.rect_answer11_a.centery = self.screen_rect.centery + 60
        self.rect_answer11_b.centerx = self.screen_rect.centerx
        self.rect_answer11_b.centery = self.screen_rect.centery + 110
        self.rect_answer11_c.centerx = self.screen_rect.centerx
        self.rect_answer11_c.centery = self.screen_rect.centery + 160

        # Load the question no 12 image and answer and get its rect.
        self.question12 = pygame.image.load("images/question12.PNG")
        self.rect_question12 = self.question12.get_rect()
        self.answer12_a = pygame.image.load("images/answer12_a.PNG")
        self.rect_answer12_a = self.answer12_a.get_rect()
        self.answer12_b = pygame.image.load("images/answer12_b.PNG")
        self.rect_answer12_b = self.answer12_b.get_rect()
        self.answer12_c = pygame.image.load("images/answer12_c.PNG")
        self.rect_answer12_c = self.answer12_c.get_rect()
        # Play button location
        self.rect_question12.centerx = self.screen_rect.centerx
        self.rect_question12.centery = self.screen_rect.centery - 100
        self.rect_answer12_a.centerx = self.screen_rect.centerx
        self.rect_answer12_a.centery = self.screen_rect.centery + 60
        self.rect_answer12_b.centerx = self.screen_rect.centerx
        self.rect_answer12_b.centery = self.screen_rect.centery + 110
        self.rect_answer12_c.centerx = self.screen_rect.centerx
        self.rect_answer12_c.centery = self.screen_rect.centery + 160

        # Load the question no 13 image and answer and get its rect.
        self.question13 = pygame.image.load("images/question13.PNG")
        self.rect_question13 = self.question13.get_rect()
        self.answer13_a = pygame.image.load("images/answer13_a.PNG")
        self.rect_answer13_a = self.answer13_a.get_rect()
        self.answer13_b = pygame.image.load("images/answer13_b.PNG")
        self.rect_answer13_b = self.answer13_b.get_rect()
        self.answer13_c = pygame.image.load("images/answer13_c.PNG")
        self.rect_answer13_c = self.answer13_c.get_rect()
        # Play button location
        self.rect_question13.centerx = self.screen_rect.centerx
        self.rect_question13.centery = self.screen_rect.centery - 100
        self.rect_answer13_a.centerx = self.screen_rect.centerx
        self.rect_answer13_a.centery = self.screen_rect.centery + 60
        self.rect_answer13_b.centerx = self.screen_rect.centerx
        self.rect_answer13_b.centery = self.screen_rect.centery + 110
        self.rect_answer13_c.centerx = self.screen_rect.centerx
        self.rect_answer13_c.centery = self.screen_rect.centery + 160

        # Load the question no 14 image and answer and get its rect.
        self.question14 = pygame.image.load("images/question14.PNG")
        self.rect_question14 = self.question14.get_rect()
        self.answer14_a = pygame.image.load("images/answer14_a.PNG")
        self.rect_answer14_a = self.answer14_a.get_rect()
        self.answer14_b = pygame.image.load("images/answer14_b.PNG")
        self.rect_answer14_b = self.answer14_b.get_rect()
        self.answer14_c = pygame.image.load("images/answer14_c.PNG")
        self.rect_answer14_c = self.answer14_c.get_rect()
        # Play button location
        self.rect_question14.centerx = self.screen_rect.centerx
        self.rect_question14.centery = self.screen_rect.centery - 100
        self.rect_answer14_a.centerx = self.screen_rect.centerx
        self.rect_answer14_a.centery = self.screen_rect.centery + 60
        self.rect_answer14_b.centerx = self.screen_rect.centerx
        self.rect_answer14_b.centery = self.screen_rect.centery + 110
        self.rect_answer14_c.centerx = self.screen_rect.centerx
        self.rect_answer14_c.centery = self.screen_rect.centery + 160

        # Load the question no 15 image and answer and get its rect.
        self.question15 = pygame.image.load("images/question15.PNG")
        self.rect_question15 = self.question15.get_rect()
        self.answer15_a = pygame.image.load("images/answer15_a.PNG")
        self.rect_answer15_a = self.answer15_a.get_rect()
        self.answer15_b = pygame.image.load("images/answer15_b.PNG")
        self.rect_answer15_b = self.answer15_b.get_rect()
        self.answer15_c = pygame.image.load("images/answer15_c.PNG")
        self.rect_answer15_c = self.answer15_c.get_rect()
        # Play button location
        self.rect_question15.centerx = self.screen_rect.centerx
        self.rect_question15.centery = self.screen_rect.centery - 100
        self.rect_answer15_a.centerx = self.screen_rect.centerx
        self.rect_answer15_a.centery = self.screen_rect.centery - 10
        self.rect_answer15_b.centerx = self.screen_rect.centerx
        self.rect_answer15_b.centery = self.screen_rect.centery + 40
        self.rect_answer15_c.centerx = self.screen_rect.centerx
        self.rect_answer15_c.centery = self.screen_rect.centery + 90

    def start(self):
        self.screen.blit(self.play_button, self.rect_play)

    def retry(self):
        self.screen.blit(self.play_again, self.rect_play_again)

    def tutorial(self):
        self.screen.blit(self.tutorial_img, self.rect_tutorial)
        self.screen.blit(self.next, self.rect_next)

    def topics(self):
        self.screen.blit(self.operators, self.rect_operators)
        self.screen.blit(self.array, self.rect_array)
        self.screen.blit(self.loops, self.rect_loops)

    def no1(self):
        self.screen.blit(self.question1, self.rect_question1)
        self.screen.blit(self.answer1_a, self.rect_answer1_a)
        self.screen.blit(self.answer1_b, self.rect_answer1_b)
        self.screen.blit(self.answer1_c, self.rect_answer1_c)

    def no2(self):
        self.screen.blit(self.question2, self.rect_question2)
        self.screen.blit(self.answer2_a, self.rect_answer2_a)
        self.screen.blit(self.answer2_b, self.rect_answer2_b)
        self.screen.blit(self.answer2_c, self.rect_answer2_c)

    def no3(self):
        self.screen.blit(self.question3, self.rect_question3)
        self.screen.blit(self.answer3_a, self.rect_answer3_a)
        self.screen.blit(self.answer3_b, self.rect_answer3_b)
        self.screen.blit(self.answer3_c, self.rect_answer3_c)

    def no4(self):
        self.screen.blit(self.question4, self.rect_question4)
        self.screen.blit(self.answer4_a, self.rect_answer4_a)
        self.screen.blit(self.answer4_b, self.rect_answer4_b)
        self.screen.blit(self.answer4_c, self.rect_answer4_c)

    def no5(self):
        self.screen.blit(self.question5, self.rect_question5)
        self.screen.blit(self.answer5_a, self.rect_answer5_a)
        self.screen.blit(self.answer5_b, self.rect_answer5_b)
        self.screen.blit(self.answer5_c, self.rect_answer5_c)

    def no6(self):
        self.screen.blit(self.question6, self.rect_question6)
        self.screen.blit(self.answer6_a, self.rect_answer6_a)
        self.screen.blit(self.answer6_b, self.rect_answer6_b)
        self.screen.blit(self.answer6_c, self.rect_answer6_c)

    def no7(self):
        self.screen.blit(self.question7, self.rect_question7)
        self.screen.blit(self.answer7_a, self.rect_answer7_a)
        self.screen.blit(self.answer7_b, self.rect_answer7_b)
        self.screen.blit(self.answer7_c, self.rect_answer7_c)

    def no8(self):
        self.screen.blit(self.question8, self.rect_question8)
        self.screen.blit(self.answer8_a, self.rect_answer8_a)
        self.screen.blit(self.answer8_b, self.rect_answer8_b)
        self.screen.blit(self.answer8_c, self.rect_answer8_c)

    def no9(self):
        self.screen.blit(self.question9, self.rect_question9)
        self.screen.blit(self.answer9_a, self.rect_answer9_a)
        self.screen.blit(self.answer9_b, self.rect_answer9_b)
        self.screen.blit(self.answer9_c, self.rect_answer9_c)

    def no10(self):
        self.screen.blit(self.question10, self.rect_question10)
        self.screen.blit(self.answer10_a, self.rect_answer10_a)
        self.screen.blit(self.answer10_b, self.rect_answer10_b)

    def no11(self):
        self.screen.blit(self.question11, self.rect_question11)
        self.screen.blit(self.answer11_a, self.rect_answer11_a)
        self.screen.blit(self.answer11_b, self.rect_answer11_b)
        self.screen.blit(self.answer11_c, self.rect_answer11_c)

    def no12(self):
        self.screen.blit(self.question12, self.rect_question12)
        self.screen.blit(self.answer12_a, self.rect_answer12_a)
        self.screen.blit(self.answer12_b, self.rect_answer12_b)
        self.screen.blit(self.answer12_c, self.rect_answer12_c)

    def no13(self):
        self.screen.blit(self.question13, self.rect_question13)
        self.screen.blit(self.answer13_a, self.rect_answer13_a)
        self.screen.blit(self.answer13_b, self.rect_answer13_b)
        self.screen.blit(self.answer13_c, self.rect_answer13_c)

    def no14(self):
        self.screen.blit(self.question14, self.rect_question14)
        self.screen.blit(self.answer14_a, self.rect_answer14_a)
        self.screen.blit(self.answer14_b, self.rect_answer14_b)
        self.screen.blit(self.answer14_c, self.rect_answer14_c)

    def no15(self):
        self.screen.blit(self.question15, self.rect_question15)
        self.screen.blit(self.answer15_a, self.rect_answer15_a)
        self.screen.blit(self.answer15_b, self.rect_answer15_b)
        self.screen.blit(self.answer15_c, self.rect_answer15_c)