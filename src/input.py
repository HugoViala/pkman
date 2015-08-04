import pygame

class UserInput:
    """ store the input entered by the user for one frame """
    def __init__(self):
        self.move_up = False
        self.move_left = False
        self.move_down = False
        self.move_right = False
        self.action = False
        self.use_controller = False
        self.dt = 0.03333333  # NOTE(hugo): the time (in s) between two frames

    def processEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left = True
            if event.key == pygame.K_UP:
                self.move_up = True
            if event.key == pygame.K_RIGHT:
                self.move_right = True
            if event.key == pygame.K_DOWN:
                self.move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_left = False
            if event.key == pygame.K_UP:
                self.move_up = False
            if event.key == pygame.K_RIGHT:
                self.move_right = False
            if event.key == pygame.K_DOWN:
                self.move_down = False

    def reset(self):
        self.__init__()
