import pygame
import input

if __name__ == "__main__":

    pygame.init()
    clock = pygame.time.Clock()
    window_size = (700, 500)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("PKMAN")
    game_running = True
    user_input = input.UserInput()
    while game_running:
        user_input.reset()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            else:
                user_input.processEvent(event)
        screen.fill((255, 255, 255))
        pygame.display.flip()
        if user_input.move_up:
            print "UP"
        clock.tick(60)
    pygame.quit()
