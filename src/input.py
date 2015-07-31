import pygame

class UserInput:
    """ store the input entered by the user for one frame """
    def __init__(self):
        self.move_up = False
        self.move_left = False
        self.move_down = False
        self.move_up = False
        self.action = False
        self.use_controller = False
    pass
def processInput():
    user_input = UserInput()
    print user_input.move_up
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                user_input.move_left = True
            if event.key == pygame.K_UP:
                user_input.move_up = True
            if event.key == pygame.K_RIGHT:
                user_input.move_right = True
            if event.key == pygame.K_DOWN:
                user_input.move_down = True
    return user_input
