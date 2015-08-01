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
    # TODO(hugo): create a Player class ? at least handling speed and velocity
    if user_input.move_up:
        player.p.y -= 5
    if user_input.move_down:
        player.p.y += 5
    if user_input.move_left:
        player.p.x -= 5
    if user_input.move_right:
        player.p.x += 5
    player_rect = pygame.Rect(player.p.x, player.p.y, player.w, player.h)
    window_surface.fill((255, 0, 0), player_rect)
    return (player.p.x, player.p.y)
