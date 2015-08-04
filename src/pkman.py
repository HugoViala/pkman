import pygame
import input
import game
import pkcolor

# TODO(hugo): make it so that game module does not have to import pygame ?
# like, the updateAndRender function could return the game state and the list
# of the rect do display for the window_surface => cleaner
# TODO(hugo): the rendering is buggy is the upper and left border of the
# window

if __name__ == "__main__":

    # NOTE(hugo): initializing lots of stuff
    pygame.init()
    clock = pygame.time.Clock()
    window_size = (700, 500)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("PKMAN")
    gamestate = game.GameState()
    user_input = input.UserInput()
    window_surface = pygame.display.get_surface()
    frame_per_second = 30

    while gamestate.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamestate.running = False
            if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP) and event.key == pygame.K_q:
                gamestate.running = False
            else:
                user_input.processEvent(event)
        screen.fill(pkcolor.white)
        game.updateAndRender(user_input, window_surface, gamestate)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
