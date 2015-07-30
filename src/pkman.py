import pygame

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    window_size = (700, 500)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("PKMAN")
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        screen.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
