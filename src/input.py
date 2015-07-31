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

    def reset(self):
        self.__init__()
