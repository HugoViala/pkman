import pygame
import pkmath

# TODO(hugo): support gamepad
# TODO(hugo): support re-mapping keys in the future
class UserInput:
    """ store the input entered by the user for one frame """
    def __init__(self):
        self.move_up = False
        self.move_left = False
        self.move_down = False
        self.move_right = False
        self.action = False
        self.use_controller = False
        self.axis_motion = pkmath.v2()
        self.dt = 0.03333333  # NOTE(hugo): the time (in s) between two frames
        # NOTE(hugo): joystick init
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for joy in self.joysticks:
            joy.init()

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
        if event.type == pygame.JOYAXISMOTION:
            # TODO(hugo): still a few bugs to investigate
            # maybe they are related to deadzones or with the
            # implementation in game.py module...
            self.use_controller = True
            if event.dict["value"] >= 0.1  or event.dict["value"] <= -0.1:
                if event.dict["axis"] == 0:
                    self.axis_motion.x = event.dict["value"]
                elif event.dict["axis"] == 1:
                    self.axis_motion.y = event.dict["value"]
            else:
                self.axis_motion = pkmath.v2()
            print(self.axis_motion.x, self.axis_motion.y)

    def reset(self):
        self.__init__()

    def reset_axis(self):
        self.axis_motion = pkmath.v2()
