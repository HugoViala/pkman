import pygame
import pkmath

class Player:
    """ class to handle all the details about a player entity """
    def __init__(self, x, y, w, h):
        self.p = pkmath.v2(x, y)
        self.dp = pkmath.v2(0, 0)
        self.w = w
        self.h = h


def updateAndRender(user_input, window_surface,
                    player):
    """ update the game and render the current frame """
    # TODO(hugo): improve it so that we can enter both direction
    # TODO(hugo): maybe consider acceleration and equations of motion
    player.dp = pkmath.v2(0, 0)
    if user_input.move_up:
        player.dp = pkmath.v2(0, -50)
    if user_input.move_down:
        player.dp = pkmath.v2(0, 50)
    if user_input.move_left:
        player.dp = pkmath.v2(-50, 0)
    if user_input.move_right:
        player.dp = pkmath.v2(50, 0)
    player.p = pkmath.add(player.p, pkmath.times(user_input.dt, player.dp))
    player_rect = pygame.Rect(player.p.x, player.p.y, player.w, player.h)
    window_surface.fill((255, 0, 0), player_rect)
    return (player.p.x, player.p.y)
