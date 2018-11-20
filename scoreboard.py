import pygame.font

class Scoreboard():
    """A class to report scoring information."""
    def __init__(self, ai_settings, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.correct = 0
        self.wrong = 0
        self.score = 0

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.wrong_color = (192, 0, 0)
        self.correct_color = (56, 87, 35)
        self.font1 = pygame.font.SysFont("ArcadeClassic", 70)
        self.font2 = pygame.font.SysFont("ArcadeClassic", 28)
        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = "{:7}{:,}".format("Score ",int(self.score))
        self.score_image = self.font1.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        correct_str = "{:16}{:,}".format("Correct Answer ", int(self.correct))
        self.correct_image = self.font2.render(correct_str, True, self.correct_color,
                                            self.ai_settings.bg_color)

        wrong_str = "{:14}{:,}".format("Wrong Answer ", int(self.wrong))
        self.wrong_image = self.font2.render(wrong_str, True, self.wrong_color,
                                              self.ai_settings.bg_color)


        # Display the score.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.centery = self.screen_rect.centery - 80

        # Display the correct answer.
        self.correct_rect = self.correct_image.get_rect()
        self.correct_rect.centerx = self.screen_rect.centerx
        self.correct_rect.centery = self.screen_rect.centery - 40

        # Display the wrong answer.
        self.wrong_rect = self.wrong_image.get_rect()
        self.wrong_rect.centerx = self.screen_rect.centerx
        self.wrong_rect.centery = self.screen_rect.centery - 10

    def reset_score(self):
        self.score = 0
        self.wrong = 0
        self.correct = 0

    def title(self):
        self.myfont = pygame.font.SysFont('ArcadeClassic', 72)
        self.textsurface = self.myfont.render('PYTHON QUIZ GAME', False, (0, 0, 0))
        self.textsurface_rect = self.textsurface.get_rect()
        self.textsurface_rect.centerx = self.screen_rect.centerx
        self.textsurface_rect.centery = self.screen_rect.centery + 130

        self.screen.blit(self.textsurface, (self.textsurface_rect))

    def show_score(self):
        """Draw score to the screen."""
        self.prep_score()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.correct_image, self.correct_rect)
        self.screen.blit(self.wrong_image, self.wrong_rect)