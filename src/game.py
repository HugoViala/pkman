import pygame

def updateAndRender(user_input, window_surface,
                    player_x, player_y, player_w, player_h):
    """ update the game and render the current frame """
    if user_input.move_up:
        player_y -= 5
    if user_input.move_down:
        player_y += 5
    if user_input.move_left:
        player_x -= 5
    if user_input.move_right:
        player_x += 5
    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
    window_surface.fill((255, 0, 0), player_rect)
    return (player_x, player_y)
